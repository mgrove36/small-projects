// © Matthew Grove 2022

String.prototype.replaceAt = function(index, replacement) {
    return this.substr(0, index) + replacement + this.substr(index + replacement.length);
}
const delay = ms => new Promise(resolve => setTimeout(resolve, ms));

let turingMachine = class {
    /**
     * Constructs a turing machine class object.
     * @param {tape} String A string containing the contents of the tape.
     * @param {transitions} String A string containing the transition functions for the machine.
     *                          States are separated by / and transition functions are separated by ,
     *                          Each transition function must contain four characters: input character, output character, direction to move (l or r), and state to transition into
     *                          States are numbered automatically by index, and accepting states must be defined with no transition functions
     * @param {startPosition} Integer The starting index of the pointer on the tape.
     * @param {startState} Integer The index of the machine's starting state.
     * @param {delay} Integer The time period (in ms) to wait before each transition.
     */
    constructor(tape, transitions, startPosition, startState, delay) {
        this.position = startPosition;
        this.tape = tape;
        let exportedTransitions = {};
        transitions.split("/").map((state, stateIndex) => {
            if (state.length > 0) {
                exportedTransitions[stateIndex] = {
                    accepting: false,
                };
                state.split(",").map(transition => {
                    exportedTransitions[stateIndex][transition.charAt(0)] = {
                        write: transition.charAt(1),
                        move: transition.charAt(2),
                        newState: transition.charAt(3),
                    };
                }, this);
            } else {
                exportedTransitions[stateIndex] = {
                    accepting: true,
                };
            }
        }, this);
        this.transitions = exportedTransitions;
        this.state = startState;
        this.delay = delay;
    }

    run = async () => {
        console.log(`Machine is now running. Tape is currently:
${this.tape}
${" ".repeat(this.position)}^`);
        while (!this.transitions[this.state].accepting) {
            await delay(this.delay);
            let transitionData = this.transitions[this.state][this.tape.charAt(this.position)]; // storing write, move, newState
            let originalChar = this.tape.charAt(this.position);
            this.tape = this.tape.replaceAt(this.position, transitionData.write);
            // shift position
            if (transitionData.move.toLowerCase() === "l") {
                if (this.position === 0) {
                    this.tape = ` ${this.tape}`;
                } else {
                    this.position--;
                }
            } else {
                this.position++;
                if (this.position == this.tape.length) {
                    this.tape = `${this.tape} `;
                }
            }
            console.log(`Read ${originalChar} at position ${this.position} in state ${this.state}, and changed it to ${transitionData.write}. Machine has moved to state ${transitionData.newState} and tape is now:
${this.tape}
${" ".repeat(this.position)}^`)
            this.state = transitionData.newState;
        }

        if (this.transitions[this.state].accepting) {
            console.log(`Machine is accepting in state ${this.state}. Tape is now:
${this.tape}
${" ".repeat(this.position)}^`)
        } else {
            console.log("error...")
        }
    }
}

let machineOne = new turingMachine("01#    ", "00r0,11r0,##r0, 0l2/00r1,11r1,##r1, 1l2/00l2,11l2,##l2,x0r3,y1r3/0xr0,1yr1,##r4/",0,3, 1000);
machineOne.run();