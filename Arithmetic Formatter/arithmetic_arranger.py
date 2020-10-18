import re

pad = " "*4


def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        line1 = ""
        line2 = ""
        line3 = ""

        if solve:
            line4 = ""

        for p in problems:
            ops = p.split(" ")
            num1 = ops[0]
            num2 = ops[2]
            operator = ops[1]

            if not (operator == "+" or operator == "-"):
                return "Error: Operator must be \'+\' or \'-\'."
            elif re.search(r'\D+', num1) is not None or re.search(r'\D+', num2) is not None:
                return "Error: Numbers must only contain digits."
            elif len(str(num1)) > 4 or len(str(num2)) > 4:
                return "Error: Numbers cannot be more than four digits."
            else:
                if solve:
                    res = eval(p)

                max_length = max(len(num1), len(num2))

                if len(num1) < len(num2):
                    line1 += "{:>{rjust}}{}".format(num1,
                                                    pad, rjust=len(num2)+2)
                    line2 += "{}{:>{rjust}}{}".format(
                        operator, num2, pad, rjust=len(num2) + 1)
                else:
                    line1 += "{:>{rjust}}{}".format(num1,
                                                    pad, rjust=len(num1)+2)
                    line2 += "{}{:>{rjust}}{}".format(
                        operator, num2, pad, rjust=len(num1) + 1)
                line3 += "-" * (max_length + 2) + pad
                if solve:
                    line4 += "{:>{rjust}}{}".format(res,
                                                    pad, rjust=max_length + 2)

    return line1[:-4] + "\n" + line2[:-4] + "\n" + line3[:-4] + ("\n" + line4[:-4] if solve else "")
