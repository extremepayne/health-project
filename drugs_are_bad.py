"""Say things about drugs being bad."""
# pylint: disable=C0103
DRUG_FACTS = {
    "alcohol": [
        "Banning alcohol would save more lives than gun control.",  # This
        "Banning alcohol would save more lives than gun control.",  # one
        "Banning alcohol would save more lives than gun control.",  # is
        "Banning alcohol would save more lives than gun control.",  # really
        "Banning alcohol would save more lives than gun control.",  # by
        "Banning alcohol would save more lives than gun control.",  # far
        "Banning alcohol would save more lives than gun control.",  # the
        "Banning alcohol would save more lives than gun control.",  # best.
        "Banning alcohol would save more lives than gun control.",
        "1 in 12 US adults suffer from alcohol dependence. \
        [facingaddiction.org]",
        "1 in 4 US teens report binge drinking. \
        [facingaddiction.org]",
        "Every year, 2.8 million deaths are caused by alcohol. \
        [facingaddiction.org]",
        "40% of hosiptal beds in the US are being used to treat a \
        alcohol-related condition. [facingaddiction.org]",
        "Alcohol use can lead to dementia. [facingaddiction.org]",
    ],
    "cigarettes": [
        "Using cigarettes decreases your life expectancy by 10 years. \
        [standaz.com/tobacco-facts]"
        "Cigarettes contain at least 70 carcinogens (which cause cancer.) \
        [standaz.com/tobacco-facts]",
        "Tabacco use is the leading cause of preventable death -- worldwide. \
        [standaz.com/tobacco-facts]",
        "9 in 10 smokers started before they were 18. \
        [standaz.com/tobacco-facts]",
        "7 in 10 smokers want to quit. [standaz.com/tobacco-facts]",
        "If the current trend continues, 1 in 13 americans who are teens now \
        will die prematurely from smoking-related causes. \
        [standaz.com/tobacco-facts]",
    ],
    "meth": [
        "Meth can cause extreme weight loss. [www.drugabuse.gov]",
        "Meth is linked to higher frequency of violent behavior. \
        [www.medicalnewstoday.com]",
        "Meth can cause severe dental problems. [www.medicalnewstoday.com]",
        "In 2007, 4.5% of high school seniors reported having used meth. \
        [www.drugfreeworld.org]",
    ],
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


dict_keys = list(DRUG_FACTS.keys())
drug = ask("What drug is being used? ", str.lower, range_=dict_keys)
if drug == "alcohol":
    pass
elif drug == "cigarettes":
    pass
else:  # meth
    pass
input("Press enter to exit.")
