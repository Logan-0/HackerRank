use std::io;

// try building programs to do the following:

// Generate the nth Fibonacci number.
// Print the lyrics to the Christmas carol “The Twelve Days of Christmas,” taking advantage of the repetition in the song.

fn main() {
    loop {
        let array = [0, 1];

        println!("Please input your length of Fib(n): ");
        let mut fib: String = String::new();
        io::stdin()
            .read_line(&mut fib)
            .expect("Failed to read line");

        let fib: i32 = fib.trim().parse().expect("Input was not a number!");

        let mut new_vector = Vec::new();
        new_vector.extend(array);

        for _n in 0..fib - 2 {
            new_vector.push(0);
        }

        print_array(&new_vector);

        let mut count: i32 = 1;

        for element in new_vector {
            let new_element = array[count as usize] + array[count as usize - 1];

            let mut vector = new_vector;

            println!("Element {}", element);
            println!("New Element {}", new_element);
            println!("Count {}", count);

            vector[count as usize + 1] = new_element;

            count = count + 1;
        }
    }
}

fn print_array<T: std::fmt::Display>(v: &Vec<T>) {
    for (count, element) in v.iter().enumerate() {
        println!("Element {} is {}", count, element);
    }
}
