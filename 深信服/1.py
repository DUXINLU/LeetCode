def find_diff_char(self, str1, str2):
    str1, str2 = list(str1), list(str2)
    str1.sort()
    str2.sort()
    l1, l2 = len(str1), len(str2)

    for i in range(min(l1, l2)):
        if str1[i] != str2[i]:
            # add
            if l1 < l2:
                print(str2[i])
                return
            # delete
            else:
                print(str1[i])
                return
    if l1 < l2:
        print(str2[-1])
        return
    else:
        print(str1[-1])
        return


find_diff_char('', 'kjgfytygchgc', 'kjgfytygchgcz')
