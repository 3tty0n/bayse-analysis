library(rstan)

d <- read.csv('input/data_example1_fit.csv')
N <- nrow(d)
K <- 7
PRE <- d$prefectures
data <- list(N=N,
             K=K, 
             X=d$population, 
             Y=d$finance, PRE=PRE)

fit <- stan(file='model/bayes-mcmc.stan',
            data=data, 
            seed=12345)

save.image(file='output/result-bayes-mcmc.RData')
