## Brainstorming and resources for future 100 Days work  


**Golf Case Study**  
This is a little bit of gold from Andrew Gelman. He builds up a putting model with a golfer's perspective. Love this.  

  - Discussion on Gelman's blog: https://statmodeling.stat.columbia.edu/2019/10/04/golf-example-now-a-stan-case-study/  
  - Case study: https://mc-stan.org/users/documentation/case-studies/golf.html  

**Stan Case Studies**  
These will certainly be worth a look: https://mc-stan.org/users/documentation/case-studies  

**Bayesian Methods for Hackers**  
This has a range of examples and walkthroughs. Tough read, verbose code without enough explanation. But the goal has to be to read this and understand it. 
https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers  

**The joint log_prob function**  
This is the workhorse of TFP and is often left unexplained. Start with Chpt 2 of Bayesian Methods for Hackers, I will need to scroll down about 
half way before they start to talk through the joint_log_prob function. Then, go to the TFP docs:  

  - Define our joint log-prob function here: 
https://github.com/tensorflow/probability/blob/master/tensorflow_probability/examples/jupyter_notebooks/A_Tour_of_TensorFlow_Probability.ipynb  
  - "Connecting model building and inference in TFP": https://github.com/tensorflow/probability/blob/master/discussion/joint_log_prob.md  
  - The Challenger Space Shuttle example which has a reasonably simple joint-log-prob: 
https://medium.com/tensorflow/an-introduction-to-probabilistic-programming-now-available-in-tensorflow-probability-6dcc003ca29e  


**Estimation using TFP layers**  
This is a reasonably simple way to start with estimation. Much cleaner than the full-on TFP approach: 
https://medium.com/tensorflow/regression-with-probabilistic-layers-in-tensorflow-probability-e46ff5d37baf  


**Edward**  
This is a simpler interface to estimation, a high-level abstraction for researchers and applied peeps like me.  

  - 8 Schools example in Edward: https://github.com/tensorflow/probability/blob/master/tensorflow_probability/examples/jupyter_notebooks/Eight_Schools.ipynb  
  - 


**TFP Estimation**  
The Challenger Space Shuttle example is probably a good place to start, reasonably simple: 
https://medium.com/tensorflow/an-introduction-to-probabilistic-programming-now-available-in-tensorflow-probability-6dcc003ca29e  

And I loved this one which compares lme4, Stan and TFP: (can't find right now...)


**Bijectors**  
These will be fun to tackle. There is a nice example of a bijector transforming a distribution here: 
https://github.com/tensorflow/probability/blob/master/tensorflow_probability/examples/jupyter_notebooks/A_Tour_of_TensorFlow_Probability.ipynb
