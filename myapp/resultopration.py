def per(obtain,max,resultobj=None):
    status = ''
    per = ((obtain*100)/max)
    print()
    if per<33:
        status = 'Failed'
    if per>=33 and per<50:
        status = 'passed with Third division'
    if per>=50 and per<60:
        status = 'passed with second division'
    if per>=60 and per<=100:
        status = 'passed with First division'
    count = 0
    obtotal = 0
    mxtotal = 0
    if resultobj is not None:
        for marks in resultobj:
            obtain = int(marks.obtain_marks)
            obtotal += (obtain)
            max = int(marks.max_marks)
            mxtotal += max
            if float(max)>0:
                pers = ((float(obtain)*100)/float(max))
                if pers<33:
                    count += 1
                    if count<2:
                        status = 'supplementary'
                    else:
                        status = 'Failed'
    res = {
        'ob_total':obtotal,
        'mx_total':mxtotal,
        'percent' :str(per),
        'status':status
    }
    return res