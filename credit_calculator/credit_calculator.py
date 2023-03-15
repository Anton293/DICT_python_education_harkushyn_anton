import math
import argparse
import re


def pluralize(count: int, text: str) -> str:
    """pluralize function"""
    return f"{count} {text}{'s' if count != 1 else ''}"


def months_to_years_months(number_month: int) -> str:
    """Converts the given number of months into years and months.
    
    Args:
        number_month (int): The number of months to convert.
        
    Returns:
        str: A string representing the number of years and months.
    """
    if number_month <= 0:
        raise ValueError("Number of months must be greater than zero.")

    months_in_year = 12
    years = number_month // months_in_year
    months = number_month % months_in_year

    result = []
    if years > 0:
        result.append(pluralize(years, 'year'))
    if months > 0:
        result.append(pluralize(months, 'month'))

    result_str = ' and '.join(result)
    return f"It will take {result_str} to repay this loan!"


class CreditCalculator(object):
    @staticmethod
    def calculate_annuity_payment(principal, periods, interest) -> int:
        """annuity payment calculation formula"""
        r = interest / (12 * 100)
        numerator = r * ((1 + r) ** periods)
        denominator = ((1 + r) ** periods) - 1
        annuity_payment = math.ceil(principal * (numerator / denominator))
        return annuity_payment

    @staticmethod
    def calculate_loan_principal(payment, periods, interest) -> int:
        """loan principal calculation formula"""
        r = interest / (12 * 100)
        numerator = r * ((1 + r) ** periods)
        denominator = ((1 + r) ** periods) - 1
        loan_principal = math.floor(payment / (numerator / denominator))
        return loan_principal

    @staticmethod
    def calculate_diff_payment(principal, periods, interest, month) -> int:
        """differentiated payment calculation formula"""
        i = interest / (12 * 100)
        diff_payment = math.ceil((principal / periods) + i * (principal - ((principal * (month - 1)) / periods)))
        return diff_payment

    @staticmethod
    def calculate_loan_periods(principal, payment, interest) -> int:
        """loan periods calculation formula"""
        r = interest / (12 * 100)
        numerator = payment - r * principal
        denominator = payment / numerator
        periods = math.ceil(math.log(denominator, 1 + r))
        return periods
    
    @staticmethod
    def calculate_overpayment(principal, periods, interest, payment) -> int:
        """overpayment calculation formula"""
        overpayment = (payment * periods) - principal
        return overpayment
        
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', choices=['annuity', 'diff'], help='The type of payment')
    parser.add_argument('--principal', type=int, help='The principal amount of the loan')
    parser.add_argument('--periods', type=int, help='The number of periods to repay the loan')
    parser.add_argument('--interest', type=float, help='The interest rate of the loan')
    parser.add_argument('--payment', type=int, help='The monthly payment amount')

    # get argument terminal
    args = parser.parse_args()
    
    count_not_found_arguments = len(re.findall(r'\bNone\b', str(args)))
    if count_not_found_arguments > 1:
        #check args min 4
        raise ValueError("Incorrect parameters")
    elif not args.interest:
        #check args interest
        raise ValueError("Incorrect parameters")
    elif re.findall(r'\b=-\b', str(args)):
        #search '-'
        raise ValueError("Incorrect parameters")
    elif args.payment is not None and args.type == "diff":
        #check -> not payment in diff
        raise ValueError("Incorrect parameters")
    elif not args.type:
        #check type
        raise ValueError("Incorrect parameters")


    if args.type == 'annuity':
        if not args.payment:
            annuity_payment = CreditCalculator().calculate_annuity_payment(args.principal, args.periods, args.interest)
            overpayment = CreditCalculator().calculate_overpayment(args.principal, args.periods, args.interest, annuity_payment)
            print(f'Your annuity payment = {annuity_payment}!\nOverpayment = {overpayment}')

        elif not args.principal:
            loan_principal = CreditCalculator().calculate_loan_principal(args.payment, args.periods, args.interest)
            overpayment = CreditCalculator().calculate_overpayment(loan_principal, args.periods, args.interest, args.payment)
            print(f'Your loan principal = {loan_principal}!\nOverpayment = {overpayment}')

        elif not args.periods:
            loan_periods = CreditCalculator().calculate_loan_periods(args.principal, args.payment, args.interest)
            overpayment = CreditCalculator().calculate_overpayment(args.principal, loan_periods, args.interest, args.payment)
            print(f"{months_to_years_months(loan_periods)}\nOverpayment = {overpayment}")

    elif args.type == 'diff':
        total_overpayment = 0
        for m in range(1, args.periods + 1):
            diff_payment = CreditCalculator().calculate_diff_payment(args.principal, args.periods, args.interest, m)
            total_overpayment += diff_payment - (args.principal / args.periods)
            print(f'Month {m}: payment is {diff_payment}')
        print(f'\nOverpayment = {total_overpayment}')


if __name__ == "__main__":
    main()
