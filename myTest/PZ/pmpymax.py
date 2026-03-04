import concore

concore.delay = 0.01
concore.default_maxtime(100)
#Nsim = 100
init_simtime_u = "[0.0, 0.0, 0.0]"
init_simtime_ym = "[0.0, 0.0, 0.0]"

ym = concore.initval(init_simtime_ym)
while(concore.simtime<concore.maxtime):
    while concore.unchanged():
        u_result = concore.read(1,"u",init_simtime_u)
        u = u_result[0] if isinstance(u_result, tuple) else u_result
    ym[0]  = u[0]+10000
    print("ym="+str(ym[0])+" u="+str(u[0]));
    concore.write(1,"ym",ym,delta=1)
print("retry="+str(concore.retrycount))
