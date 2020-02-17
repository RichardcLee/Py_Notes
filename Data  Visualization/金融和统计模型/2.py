from decimal import Decimal
import matplotlib.pyplot as plt

colors = [(31, 119, 180), (174, 199, 232), (255, 128, 0), (255, 15, 14), (44, 160, 44), (152, 223, 138), (214, 39, 40),
          (255, 173, 61), (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148), (227, 119, 194), (247, 182, 210),
          (127, 127, 127), (199, 199, 199), (188, 189, 34), (219, 219, 141), (23, 190, 207), (15, 218, 229), [217, 217, 217]]

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
for i in range(len(colors)):
    r, g, b = colors[i]
    colors[i] = (r/255., g/255., b/255.)


# def printHeaders(term, extra):
#     # print headers
#     print('\nExtra-Payment: $'+str(extra)+" Term:"+str(term)+" years")
#     print('---------------------------------------------------------')
#     print('pmy no'.rjust(6), ' ', 'Beg. bal.'.ljust(13), ' ')
#     print('Payment'.ljust(9), ' ', 'Principal'.ljust(9), ' ')
#     print('Interest'.ljust(9), ' ', 'End. bal.'.ljust(13))
#     print(''.rjust(6, '-'), ' ', ''.ljust(13, '-'), ' ')
#     print(''.ljust(9, '-'), ' ', ''.ljust(9, '-'), ' ')
#     print(''.ljust(9, '-'), ' ', ''.ljust(13, '-'), ' ')


def amortization_table(principal, rate, term, extrapayment, printData=False):
    '''
    :param principal: 贷款金额
    :param rate: 偿还利率×100
    :param term: 期限（月数）
    :param extrapayment: 每月额外支付
    :param printData:
    :return:
    '''
    xarr = []
    begarr = []

    original_loan = principal
    money_saved = 0     # 节省的金额
    total_payment = 0   # 总共偿还金额
    payment = pmt(principal, rate, term)    # 每期应付额
    begBal = principal  # 贷款未还总额

    num = 1  # 当前偿还期数
    endBal = 1  #
    # if printData == True:
    #     printHeaders(term, extrapayment)

    while (num < term + 1) and (endBal > 0):
        interest = round(begBal * Decimal(rate / (12 * 100.0)), 2)    # 本期应还利息
        applied = extrapayment + round(payment - Decimal(interest), 2)   # 本期偿还金额
        endBal = round(begBal - applied, 2)     # 偿还本期后剩余的未还金额

        # 每一年记录一次 或 下期剩余未还金额 < 本期偿还金额+额外偿还金额
        if (num-1) % 12 == 0 or (endBal < applied+extrapayment):
            begarr.append(begBal)
            xarr.append(num/12)
            # if printData == True:
            #     print('{0:3d}'.format(num).center(6))
            #     print('{0:,.2f}'.format(begBal).rjust(13), ' ')
            #     print('{0:,.2f}'.format(payment).rjust(9), ' ')
            #     print('{0:,.2f}'.format(applied).rjust(9), ' ')
            #     print('{0:,.2f}'.format(interest).rjust(9), ' ')
            #     print('{0:,.2f}'.format(endBal).rjust(13))
        total_payment += applied + extrapayment
        num += 1
        begBal = endBal

    if extrapayment > 0:
        money_saved = abs(original_loan-total_payment)
        print('\nTotal Payment:', '{0:,.2f}'.format(total_payment).rjust(13))
        print(' Money Saved:', '{0:,.2f}'.format(money_saved).rjust(13))
    return xarr, begarr, '{0:,.2f}'.format(money_saved)


def pmt(principle, rate, term):
    # 每个月的利息
    ratePerTwevle = rate / (12 * 100.0)

    # 每个月应还
    result = principle * (ratePerTwevle / (1 - (1 + ratePerTwevle) ** (-term)))

    result = Decimal(result)
    result = round(result, 2)
    return result


plt.figure()

i = 0
markers = ['o', 's', 'D', '^', 'v', '*', 'p', 's', 'D', 'o', 's', 'D', '^', 'v', '*', 'p', 's', 'D']
markersize = [6, 6, 6, 10, 6, 6, 6, 10, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

for extra in range(100, 1700, 100):
    # 贷款$350000，利率5%，30年还清（360月），每月额外偿还$extra
    xv, bv, saved = amortization_table(350000, 5, 360, extra, False)
    if extra == 0:
        plt.plot(xv, bv, color=colors[i], lw=1.2, label='Principal only', marker=markers[i], markersize=markersize[i])
    else:
        plt.plot(xv, bv, color=colors[i], lw=1.2, label='Principle plus\$'+str(extra)+str("/month, Saved:\$")+saved,
                 marker=markers[i], markersize=markersize[i])
    i += 1

plt.grid(True)
plt.xlabel('years', fontsize=18)
plt.ylabel('Mortgage Balance', fontsize=18)
plt.title('Mortgage Loan for $350000 with addition payment chart')
plt.ylim(0, 350000)
plt.xlim(0, 30)
plt.legend()
plt.show()