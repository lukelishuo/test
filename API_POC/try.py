class tool():

    def listalls(self, csTrue,  csFalse):
        fzgcs = []
        listall = []
        zhcs = dict(csTrue)
        listall.append(csTrue)
        aaa = list(csFalse.keys())
        for i in aaa:
            bbb = csFalse[i]
            for k in bbb:
                fzgcs.append(k)
        print (fzgcs)
        zhcskey = list(zhcs.keys())
        for i in zhcskey:
            a = zhcs[i]
            for k in fzgcs:
                zhcs[i] = k
                listall.append(str(zhcs))
            zhcs[i] = a
        return listall

print (tool.listalls(1,{"a":"a","b":"b"},{"2":"2","3":"3","4":"4","5":"5"}))