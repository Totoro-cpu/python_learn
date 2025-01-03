def judg_whether_adult(args):
    """judge_whether_adult

    Args:
        args (int): Enter the age,
        and then determine whether
        the person is an adult based on
        whether they are 18 years old or not
    """
    if int(args) < 18:
        print("you are minors !")
    else:
        print("you are adult !")
a=10

age = input("please input your age:")
judg_whether_adult(age)
