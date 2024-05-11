use std::io;
use rand::Rng;
use std::cmp::Ordering;

// try building programs to do the following:

// Convert temperatures between Fahrenheit and Celsius.
// Generate the nth Fibonacci number.
// Print the lyrics to the Christmas carol “The Twelve Days of Christmas,” taking advantage of the repetition in the song.

fn main() {

    let secret_number = rand::thread_rng().gen_range(1..=100);

    loop {

        println!("Please input your guess.");
        let mut guess = String::new();

        io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You Win Kiddo!!");
                break;
            }
        }
    }

    
}
