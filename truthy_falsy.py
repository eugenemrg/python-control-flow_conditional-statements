def control_flow(value):
    if value:
        # if the value is truthy
        print("truthy!")
    else:
        # if the value is falsy
        print("falsy!")

control_flow(False)
# "falsy!"
control_flow(None)
# "falsy!"
control_flow(True)
# "truthy!"
control_flow("")
# "falsy!"
control_flow(0)
# "falsy!"
control_flow("0")
# "truthy!"