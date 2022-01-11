// Javascript for use


import { validateNote } from './utils.js'

/**
 * 
 * @param {string[]} elements The list of elements for get the notes
 * @returns The list of the notes for each element
 */
function getNotes(elements) {
  let notes = [];

  elements.forEach(element => {
    const e = document.querySelector(`.${element}`);
    notes.push(e); // adding

  });

  return notes;

}

// notes for get the values
const notesList = [
  'note1',
  'note2',
  'note3',
  'note4',
  'note5',
  'note6',
  'note7',
  'note8'
]

const notes = getNotes(notesList);
console.log(notes)
validateNote(notes) // validating for change the color