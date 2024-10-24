#ask for prompt
flavour <- readline("Flavor: ")
caffe <- readline("Caffeine: ")

if (flavour == "Light" & caffe == "Yes") {
  print("You might like green tea 🫖", quote = FALSE)
} else if (flavour == "Light" & caffe == "No") {
  print("You might like chamomile tea 🫖", quote = FALSE)
} else if (flavour == "Bold" & caffe == "Yes") {
  print("You might like black tea 🫖", quote = FALSE)
} else if (flavour == "Bold" & caffe == "No") {
  print("You might like rooibos tea 🫖", quote = FALSE)
} else{print("Enter Bold or Light for Flavour, Yes or No for Caffeine", quote = FALSE)
}
