def numsum(*numbrid):
    sum = 0
    for num in numbrid:
        if isinstance(num, int) or isinstance(num, float):
            sum += num
    return sum

def numcount(*numbrid):
    count = 0
    for num in numbrid:
        if isinstance(num, int) or isinstance(num, float):
            count += 1
    return count

def numavg(*numbrid):
    sum = numsum(*numbrid)
    count = numcount(*numbrid)
    result = 0.0

    try:
        result = sum / (count * 1.0)
    except ZeroDivisionError as err:
        #print("0-jagamise viga:", err)
        result = 0.0
    except:
        #print("Mingi muu viga")
        raise      # Kutsume sama vea uuesti välja
    #else:
    #    print(f"Tulemus on {result}")
    finally:
    #    print("finally")
        return result