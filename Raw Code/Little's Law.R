set.seed(1234)
process <- sample(1:100, 6, replace=T) # generate random process with 6 steps with times between 1-100 units time
# process <- c(18,59,30,21,78,10) # <- alternatively fill in your own process times

# define variables
T0 = max(process)
rb = max(process)/sum(process)
w0 = ceiling(rb*T0) # round to the nearest whole number
THw = 1/T0
maxw = w0*25

# setup arrays for each line in the plot
wip <- vector() # WIP levels
THpwc <- vector() # practical worst case throughput
THw <- vector() # worst case throughput
THb <- vector() # best case throughput

# loop through our formulas and fill the arrays
for (i in 1:maxw){
    wip[i] <- i
    pwc <- i/(w0+i-1)*rb
    THpwc[i] <- pwc
    worst <- 1/T0
    THw[i] <- worst
    if (i<w0){
        best = i/T0
    } else {
        best = rb
    }
    THb[i] <- best
}

# Plot the chart.
plot(wip, THw, col="red", lty=3, ylim = c(min(THw)/2,max(THb)*1.1))
lines(wip, THpwc, col="blue",lty=2)
lines(wip, THb, col="green", lty=3)