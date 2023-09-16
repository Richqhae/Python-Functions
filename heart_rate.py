#When you physically exercise to strengthen your heart, you should maintain your heart rate within a range for at least 20
# minutes. To find that range, subtract your age from 220. This difference is your maximum heart rate per minute. Your heart
#simply will not beat faster than this maximum (220 - age).When exercising to strengthen your heart, you should keep your heart rate between 65% and 85% of your heart’s maximum rate.#

text = input("how old are you?")
age = int(text)

maximum_rate = 220 - age
slowest_rate = 0.65 * maximum_rate
fastest_rate = 0.85 * maximum_rate

print("When you exercise to strenghten your heart, you should " + f"keep your rate rate between {slowest_rate} and {fastest_rate}" + " beats per minute.")
