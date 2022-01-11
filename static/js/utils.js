// Have utils functions for use


import { Note } from './models/note.js'

/**
 * 
 * @param {number[]} notes The notes for validate
 */
export function validateNote(notes) {

  for (let i = 0; i < notes.length; i++) {

    const valueNote = parseInt(notes[i].innerText); // getinng the note for validate
    const note = new Note(valueNote);

    if (note.value > 8) {
      // getting the name of the class
      const className = notes[i].className[12] + notes[i].className[13] + notes[i].className[14] + notes[i].className[15] + notes[i].className[16]
      const td = document.querySelector(`.${className}`)

      td.setAttribute('style', 'background-color: #aaffaa;') // setting the color

    } else if (note.value <= 8 && note.value > 5) {
      const className = notes[i].className[12] + notes[i].className[13] + notes[i].className[14] + notes[i].className[15] + notes[i].className[16]
      const td = document.querySelector(`.${className}`)

      td.setAttribute('style', 'background-color: #ffffaa;')

    } else {
      const className = notes[i].className[12] + notes[i].className[13] + notes[i].className[14] + notes[i].className[15] + notes[i].className[16]
      const td = document.querySelector(`.${className}`)

      td.setAttribute('style', 'background-color: #ffaaaa;')

    }

  }

}