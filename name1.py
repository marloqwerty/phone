
name = "gusion"
age = 19
role = ["mage", "assassin"]

print("Name : " + name.capitalize())
print("Age : " + str(age))
print("Roles : " + ', '.join(map(str.capitalize, role)) +"\n\n")


# declare a dictionary
# mage and assassin Burst and Poke, Jungler
myFavHero = {
	"name" : "harley",
	"roles" : ["mage", "assassin"],
	"specialty" : ["burst", "poke"],
	"faveLane" : "jungle"
}
print("My favorite hero is "+ myFavHero["name"].capitalize())
print("He is a good " + ' and '.join(map(str, myFavHero["roles"])))
print("He can " + ' and '.join(map(str, myFavHero["specialty"])) + " in the " + myFavHero["faveLane"])

