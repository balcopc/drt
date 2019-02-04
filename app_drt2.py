while True:
    print("Solving for distance, rate or time")
    print("-"*35)
    distA=input("Enter distance: ");rateA=input("Enter mph: ");timeA=input("Enter time: ")
    try:
        rateA=int(rateA);timeA=int(timeA);distA=rateA*timeA
    except:
        try:
            distA=int(distA);timeA=int(timeA);rateA=distA/timeA; rateA=round(rateA,1)
        except:
            try:
                distA=int(distA);rateA=int(rateA);timeA=distA/rateA;timeA=round(timeA,2)
            except:
                print("* * Need two values, no decimal. * *")
    print("-"*35)
    try:
        if timeA>=24:
            timeA=timeA/24
            timeA=round(timeA,1)
            print("Distance",distA,"Mph",rateA,"Time:",timeA,"days")
            print("-"*35)
        else:    
            print("Distance",distA,"Mph",rateA,"Time:",timeA,"hours")
            print("-"*35)
    except:
        print("Nice try, still running...)
