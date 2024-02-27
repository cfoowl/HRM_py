########################################################################################
###                                   Instructions                                   ###
########################################################################################
###                                                                                  ###
### For each two things in the INBOX, multiply them, and OUTBOX the result. Don't    ###
### worry about negative numbers for now.                                            ###
### NOTE : Interdiction d'utiliser la multiplication                                 ###
###                                                                                  ###
########################################################################################


def function(x, y):
    a = 0
    for i in range(y):
        a += x
    return a


if __name__ == "__main__":
    from libs.test import test_20

    test_20(function)
