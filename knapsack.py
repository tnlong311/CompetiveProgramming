while True:
    try:
        c, obj = map(int,input().split())
        ks = []
        for index in range(obj):
            ks.append([int(i) for i in input().split()])
            
        dp = []
        dp1 = []
        for i in range(c+1):
            dp1.append([0])

        dp.append(dp1)

        for j in range(obj):
            dp2=[]
            for i in range(c+1):
                dp3 = []
                v = ks[j][0]
                w = ks[j][1]
                if (w > i) or (dp[j][i][0] > dp[j][i-w][0] + v):
                    dp3.extend(dp[j][i])
                else:
                    dp3.extend(dp[j][i-w])
                    dp3[0] += v
                    dp3.append(j)
                dp2.append(dp3)

            dp.append(dp2)
        
        print("Dp: ",dp)
        final = dp[-1][-1][1:]
        pr =""
        for word in final:
            pr += str(word)
            pr += " "
        print(len(final))
        print(pr[:-1])
        
    except EOFError:
        break