"""Say things about drugs being bad."""
import random
import time

# pylint: disable=C0103
DRUG_FACTS = {
    "alcohol": [
        "banning alcohol would save more lives than gun control.",  # This
        "banning alcohol would save more lives than gun control.",  # one
        "banning alcohol would save more lives than gun control.",  # is
        "banning alcohol would save more lives than gun control.",  # really
        "banning alcohol would save more lives than gun control.",  # the
        "banning alcohol would save more lives than gun control.",  # best.
        "1 in 12 US adults suffer from alcohol dependence. \
[facingaddiction.org]",
        "1 in 4 US teens report binge drinking. \
[facingaddiction.org]",
        "every year, 2.8 million deaths are caused by alcohol. \
[facingaddiction.org]",
        "40% of hosiptal beds in the US are being used to treat a \
alcohol-related condition. [facingaddiction.org]",
        "alcohol use can lead to dementia. [facingaddiction.org]",
    ],
    "cigarettes": [
        "using cigarettes decreases your life expectancy by 10 years. \
[standaz.com/tobacco-facts]",
        "cigarettes contain at least 70 carcinogens (which cause cancer.) \
[standaz.com/tobacco-facts]",
        "tabacco use is the leading cause of preventable death -- worldwide. \
[standaz.com/tobacco-facts]",
        "9 in 10 smokers started before they were 18. \
[standaz.com/tobacco-facts]",
        "7 in 10 smokers want to quit. [standaz.com/tobacco-facts]",
        "if the current trend continues, 1 in 13 americans who are teens now \
will die prematurely from smoking-related causes. \
[standaz.com/tobacco-facts]",
    ],
    "meth": [
        "meth can cause extreme weight loss. [www.drugabuse.gov]",
        "meth is linked to higher frequency of violent behavior. \
[www.medicalnewstoday.com]",
        "meth can cause severe dental problems. [www.medicalnewstoday.com]",
        "in 2007, 4.5% of high school seniors reported having used meth. \
[www.drugfreeworld.org]",
    ],
    "cocaine": [
        "cocaine is the second most trafficked illegal drug in the world. \
        [drugfreeworld.org]",
        "7.5% of 12th graders report using cocaine. [drugfreeworld.org]"
        "Cocaine addiction creates $11 billion in healthcare costs in the US. \
        [michaelshouse.com]",
        "One-fourth of hospital room visits about drugs are about cocaine. \
        [michaelshouse.com]",
        "Coca-cola used to contain cocaine, and extract from the same plant \
        is still used in it today. [drugabuse.com]",
    ],
    "weed": [
        "3.8% of the world's population uses marijuana. [drugfreeworld.org]",
        "6.7% of teens are current marijuana users. [drugfreeworld.org]",
        "58% of teens say marijuana is easy to obtain. [drugfreeworld.org]",
        "40% of adult males arrested for crimes test postive for marijuana. \
        [drugfreeworld.org]",
    ],
    "heroin": [
        "There are 153,000 current users of heroin in the US. \
        [drugfreeworld.org]"
    ],
}

alcohol_types = {
    "whiskey": (25.49, "bottle"),
    "vodka": (20, "bottle"),
    "beer": (18.27, "case"),
    "wine": (15.66, "bottle"),
}

cigarette_cost = (6.95, "pack")

meth_cost = (30, "hit")

cocaine_cost = (5, "line")

weed_cost = (8, "gram")

heroin_cost = (10, "bag")

drug_types = {
    "alcohol": alcohol_types,
    "meth": meth_cost,
    "cigarettes": cigarette_cost,
    "cocaine": cocaine_cost,
    "weed": weed_cost,
    "heroin": heroin_cost,
}


def ask(prompt, type_=None, min_=None, max_=None, range_=None):
    """Get user input of a certain type, with range and min/max options."""
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError("min_ must be less than or equal to max_.")
    while True:
        ui = input(prompt)
        if type_ is not None:
            try:
                ui = type_(ui)
            except ValueError:
                print("Input type must be {0}.".format(type_.__name__))
                continue
        if max_ is not None and ui > max_:
            print("Input must be less than or equal to {0}.".format(max_))
        elif min_ is not None and ui < min_:
            print("Input must be greater than or equal to {0}.".format(min_))
        elif range_ is not None and ui not in range_:
            if isinstance(range_, range):
                template = "Input must be between {0.start} and {0.stop}."
                print(template.format(range_))
            else:
                template = "Input must be {0}."
                if len(range_) == 1:
                    print(template.format(*range_))
                else:
                    print(
                        template.format(
                            " or ".join(
                                (
                                    ", ".join(map(str, range_[:-1])),
                                    str(range_[-1]),
                                )
                            )
                        )
                    )
        else:
            return ui


def ask_yes_no(question):
    """Ask the user a yes or no question, return a boolean variable."""
    to_ask = question + "(y/n) "
    output = input(to_ask)
    while output not in ("y", "n"):
        print('That is not "y" or "n"')
        output = input(to_ask)
    if output == "y":
        rep = True
    elif output == "n":
        rep = False
    return rep


print("Welcome to Drug Cost Calculator!")
time.sleep(1)
print(
    "First, think of you or someone you know who uses drugs, cigarettes, or alcohol."
)
time.sleep(5)
keep_going = True
while keep_going:

    dict_keys = list(DRUG_FACTS.keys())
    drug = ask("What drug is being used? ", str.lower, range_=dict_keys)
    if drug == "alcohol":
        dict_keys = list(drug_types[drug].keys())
        drug_subtype = ask(
            "What kind of alcohol are you drinking? ",
            str.lower,
            range_=dict_keys,
        )
        my_str = (
            "How many "
            + drug_types[drug][drug_subtype][1]
            + "s a week are being comsumed? "
        )
        how_much = ask(my_str, int, 1, 50)
        how_long = ask("How many years has this gone on? ", float, 0.25, 70)
        cost = drug_types[drug][drug_subtype][0] * how_much * how_long * 52
        to_print = "That much drugs costs ${:,.2f}!".format(cost)
        print(to_print)
    else:  # meth or cigarettes
        my_str = (
            "How many " + drug_types[drug][1] + "s a week are being comsumed? "
        )
        how_much = ask(my_str, int, 1, 50)
        how_long = ask("How many years has this gone on? ", float, 0.25, 70)
        cost = drug_types[drug][0] * how_much * how_long * 52
        to_print = "That much drugs costs ${:,.2f}!".format(cost)
        print(to_print)

    if cost < 100:
        print(
            "You could have bought", cost // 10, "pizzas with that much money!"
        )
    elif cost < 1000:
        print(
            "You could have bought",
            cost // 100,
            "tickets to Disneyland with that much money!",
        )
    elif cost < 5000:
        print("You could have bought a vacation to NYC with that much money!")
    elif cost < 80000:
        print("You could have bought a car with that much money!")
    elif cost < 200000:
        print("You could have bought an expensive car with that much money!")
    else:
        print("You could have bought a house with that much money!")

    time.sleep(2)

    print(
        "Did you know,",
        DRUG_FACTS[drug][random.randint(0, len(DRUG_FACTS[drug]) - 1)],
    )
    keep_going = ask_yes_no("Would you like to calculate more? ")
input("Press enter to exit.")
