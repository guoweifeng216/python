def main():
    ## Analyze projectile motion.
    h0, v0 = getInput()
    print("The maximum height of the ball is " + \
          "{0:.2f} feet.".format(calculateMaximumHeight(h0, v0))) 
    print("The ball will hit the ground after approximately " + \
          "{0:.2f} seconds.".format(timeToHitGround(h0, v0)))   

def getInput():
    # Input the initial height and velocity of the ball
    h0 = eval(input("Enter the initial height of the ball: "))
    v0 = eval(input("Enter the initial velocity of the ball: "))    
    return h0, v0

def heightOfBall(h0, v0, t):
    # Return height of ball after t seconds
    return h0 + v0 * t - 16 * t * t

def calculateMaximumHeight(h0, v0):
    return heightOfBall(h0, v0, v0 / 32)

def timeToHitGround(h0, v0):
    t = .01
    while heightOfBall(h0, v0, t) >= 0:
        t += .01
    return t    

main()
