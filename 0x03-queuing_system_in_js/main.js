const person = {
  name: "jojo thomas",
  age: 25,
};

function hello() {
  console.log(`Hello my name is ${this.name} and my age is ${this.age}`);
}
const lolo = hello.bind(person);

hello();
lolo();

hello.call(person);
