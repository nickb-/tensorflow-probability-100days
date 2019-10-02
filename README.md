# tensorflow-probability-100days
### 100 Days of Experimenting with TensorFlow Probability  

I am a huge advocate for probabilistic modelling / probabilistic programming. It's a paradigm of computing which is quickly becoming "part of the new hotness" (Dillon, 2019) and is bringing fully-Bayesian machine learning up to a production-level of maturity. 

Over the past couple of years I have fully-embraced Stan. I began with Richard McElreath's course "Statistical Rethinking", for which there is [a great book](https://www.amazon.com/Statistical-Rethinking-Bayesian-Examples-Chapman/dp/1482253445), a [GitHub repo](https://github.com/rmcelreath/rethinking) and [lectures on youtube](https://www.youtube.com/watch?v=4WVelCswXo4). I then moved onto Andrew Gelman's [BDA3](https://www.amazon.com/Bayesian-Analysis-Chapman-Statistical-Science/dp/1439840954/ref=sr_1_1?keywords=bda3&qid=1570056118&s=books&sr=1-1) & using Stan itself. [Stan's documentation](https://mc-stan.org/docs/2_18/stan-users-guide/index.html) is unbelievably good.

However, some models are just too slow to be practical in the fast-paced environment that our business decisions have to be made in. As soon as we start modelling unknown variables (for example semi-supervised or fully unsupervised Hidden Markov Models), things grind to a halt. There has to be a more performant approach?!

TensorFlow Probability has been designed with three goals in mind:

  1. FAST. The team have set out to ensure that tfp is computationally fast and memory-efficient. In essence they are brining Google's engineering expertise to the world of probabilistic modelling.  
  2. Numerical stability. I will be honest, and say I don't really understand what this means :) But I trust that this is a pre-requisite of any machine learning system  
  3. Idiomatic. The team argue that tfp code "reads naturally". Hmmmm. This isn't immediately obvious to me... and this is the reason for this 100 Days of TensorFlow Probability.  
  
I am 100% willing to believe that Google's engineering team will deliver a solid language in this space. And I am willing to take all of their amazing claims at face value. And the one thing that I really, really, really like is that their initial case studies and blogs all emphasise the combination of domain knowledge with probabilistic modelling. See Arun Subramaniyan's [interview with Laurence Moroney](https://www.youtube.com/watch?v=ngFU7Rwl76g), which describes how he & his team are using probabilistic modelling to enhance their domain expertise. This is a polar opposite of a pure data-driven approach. And I love it!

But the third claim is a tough one. I understand that "idiomatic" here probably means that it is a 'natural fit with the tensorflow paradigm/language'. So perhaps, I am being a bit harsh in also interpretting this as "reads naturally". My initial foray into tfp has been quite painful - the syntax is a long way from intuitive (for me). And therefore, I am here to fix that. My goals in this repo are to slowly build my tfp-chops. To slowly, perhaps painstakingly, get to know this language and how to apply it.

And perhaps this will help someone else pick it up too!



## References

[Probabilistic Machine Learning in TensorFlow](https://www.youtube.com/watch?v=BjUkL8DFH5Q&t=4s). Josh Dillon (2019)
