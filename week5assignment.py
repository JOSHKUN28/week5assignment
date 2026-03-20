def wind_speed_report(location, daily_kmh, gale_kmh=60):
    """This funtion includes three parameters 
    and uses them to calculate some mathematical equations
    """
    loc=f"Location: {location}"
    days=f"Days: {len(daily_kmh)}"
    average=f"Average: {round(sum(daily_kmh)/len(daily_kmh), 1)}"
    peak=f"Peak speed: {max(daily_kmh)}"
    low=f"Lowest speed: {min(daily_kmh)}"
    gale_days=0
    for day in daily_kmh:
        if day>gale_kmh:
            gale_days+=1
    gale=f"Gale days: {gale_days}"
    change=[]
    for i in range(len(daily_kmh)-1):
        result=daily_kmh[i+1]-daily_kmh[i]
        change.append(result)
    final=f"Daily change: {change}"
    return loc, days, average, peak, low, gale, final
a, b, c, d, e, f, h=wind_speed_report("Aral Sea Shore", [45, 55, 72, 38, 65, 80, 50])
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(h)
