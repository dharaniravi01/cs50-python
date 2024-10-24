random_character <- function() {
  # TODO: Return one random letter

  alphabets <- letters

  #choose random letter
  random_letter <-sample(alphabets, 1)

  return(random_letter)

}

print_sequence <- function(length) {
  # TODO: Print a random sequence of specified length

  while ( length != 0){
    cat(random_character())
    Sys.sleep(0.25)
    length <- length - 1
}

}

print_sequence(20)