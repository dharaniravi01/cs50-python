#ask for meat preference
meat <- readline("Would you like chicken or beef? ")
cheese <- readline("Would you like cheese or no? ")

if (meat == "chicken" & cheese == "yes") {
print("Chicken Cheese Burger coming right away for you!!", quote = FALSE)
} else if (meat == "chicken" & cheese == "no") {
  print("Chicken Burger coming right away for you!!", quote = FALSE)
} else if (meat == "beef" & cheese == "yes") {
  print("Beef Cheese Burger coming right away for you!!", quote = FALSE)
} else if (meat == "beef" & cheese == "no") {
  print("Beef Burger coming right away for you!!", quote = FALSE)
}