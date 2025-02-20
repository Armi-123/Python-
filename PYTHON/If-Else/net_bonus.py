# "A company decided to give bonus to the employees as per the following criteria:                                                                        Time period of service                                           Bonus
#  >10 years                                                    10%
#  >=6years and <=10years                                      8%
#  Less than 6 years                                            5%
#  Ask employee for their salary and print the net bonus amount.

salary=int(input("Enter salary: "))
service=int(input("Enter experience: "))

if service>10:
    print((salary *10)/100)
elif service >= 6 and service <= 10:
    print((salary *8)/100)
elif service<6:
    print((salary *5)/100)

# elif if banne use 