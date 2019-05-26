# This is the class for combining papameter and checking the result

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

        zhcskey = list(zhcs.keys())
        for i in zhcskey:
            a = zhcs[i]
            for k in fzgcs:
                zhcs[i] = k
                listall.append(str(zhcs))
            zhcs[i] = a
        return listall