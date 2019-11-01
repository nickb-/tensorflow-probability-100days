import collections
import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import arviz as az
import matplotlib.pyplot as plt
import daft as daft 

import tensorflow as tf
import tensorflow_probability as tfp
tfd = tfp.distributions
tfb = tfp.bijectors

try:
  tf.compat.v1.enable_eager_execution()
except ValueError:
  pass

from __future__ import print_function

class MonteCarloEngine:

    def __init__(self):
        self.session = None
        self.run = tf.function(
            self.sampler, autograph=False, experimental_compile=True
        )

    def reset_session(self, config = None):
        tf.reset_default_graph()

        try:
            self.session.close()
        except:
            pass

        self.session = tf.InteractiveSession(config = config)

    def trace_function(self, samples, pkr):
        return (
            pkr.inner_results.inner_results.target_log_prob,
            pkr.inner_results.inner_results.leapfrogs_taken,
            pkr.inner_results.inner_results.has_divergence,
            pkr.inner_results.inner_results.energy,
            pkr.inner_results.inner_results.log_accept_ratio
        )

    def get_trace_stats(self, trace, statnames = ['log_likelihood', 'tree_size', 'diverging', 'energy', 'mean_tree_accept']):
      return az.from_dict(sample_stats = {k:v.numpy().T for k, v in zip(statnames, trace)})

    def compare_models(self, traces = [], labels = []):
      return az.compare({
          lab:self.get_trace_stats(trace) for lab,trace in zip(labels, traces)
      })

    def sampler(
        self, 
        model = None,    # log-probability function
        nparams = None,  # number of parameters
        inits = None,    # initialisation for parameters
        trace_fn = None, # trace function
        iters = 2000,    # number of MCMC iterations
        warmup = 1000,   # warmup iterations
        chains = 1,
        bijectors_list = None
    ):
    
        if not isinstance(inits, list):
            inits = [0.01] * nparams

        # I don't understand this part yet...
        # Dig into this in the future
        if bijectors_list is None:
            bijectors_list = [tfb.Identity()] * nparams

        kernel = tfp.mcmc.DualAveragingStepSizeAdaptation(
            tfp.mcmc.TransformedTransitionKernel(
                inner_kernel=tfp.mcmc.NoUTurnSampler(
                    target_log_prob_fn = model,
                    step_size=1.0
                ),
                bijector=[tfb.Identity()] * nparams
            ),
            target_accept_prob=.8,
            num_adaptation_steps=np.floor(0.5*warmup),
            step_size_setter_fn=lambda pkr, new_step_size: pkr._replace(
                    inner_results=pkr.inner_results._replace(step_size=new_step_size)
                ),
            step_size_getter_fn=lambda pkr: pkr.inner_results.step_size,
            log_accept_prob_getter_fn=lambda pkr: pkr.inner_results.log_accept_ratio,
        )

        samples, trace = tfp.mcmc.sample_chain(
            num_results = iters,
            num_burnin_steps = warmup,
            current_state = inits,
            kernel = kernel,
            trace_fn = trace_fn
        )

        return [samples, trace]

mcmc_engine = MonteCarloEngine()