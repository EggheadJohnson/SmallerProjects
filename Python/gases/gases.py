
def ideal(p, v, n, t):
    pressure = p*1.
    volume = v*1.
    moles = n*1.
    temperature = t*1.
    idealGasConstant = 0.08206
    if pressure == 0:
        pressure = moles*idealGasConstant*temperature/volume
        return "The pressure is "+str(pressure)
    if volume == 0:
        volume = moles*idealGasConstant*temperature/pressure
        return "The volume is "+str(volume)
    if moles == 0:
        moles = pressure*volume/(idealGasConstant*temperature)
        return "The number of moles is "+str(moles)
    if temperature == 0:
        temperature = pressure*volume/(idealGasConstant*moles)
        return "The temperature is "+str(temperature)

def combined(p1, v1, t1, p2, v2, t2):
    pressure_init = p1*1.
    pressure_final= p2*1.
    temperature_init = t1*1.
    temperature_final= t2*1.
    volume_init = v1*1.
    volume_final= v2*1.
    if pressure_init == 0:
        pressure_init = temperature_init*pressure_final*volume_final/(volume_init*temperature_final)
        return "The initial pressure was "+str(pressure_init)
    if pressure_final == 0:
        pressure_final = pressure_init*volume_init*temperature_final/(temperature_init*volume_final)
        return "The final pressure is "+str(pressure_final)
    if volume_init == 0:
        volume_init = temperature_init*pressure_final*volume_final/(pressure_init*temperature_final)
        return "The initial volume was "+str(volume_init)
    if volume_final == 0:
        volume_final = pressure_init*volume_init*temperature_final/(temperature_init*pressure_final)
        return "The final volume is "+str(volume_final)
    if temperature_init == 0:
        temperature_init = pressure_init*volume_init*temperature_final/(volume_final*pressure_final)
        return "The initial temperature was "+str(temperature_init)
    if temperature_final == 0:
        temperature_final = temperature_init*pressure_final*volume_final/(pressure_init*volume_init)
        return "The final temperature is "+str(temperature_final)
