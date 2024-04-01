from flask import Flask, request, jsonify
 
 
app = Flask(__name__)
 
# Sample data stored in memory
notes = []
 
# Routes
@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)
 
@app.route('/notes', methods=['POST'])
def add_note():
    data = request.get_json()
    new_note = {
        'id': len(notes) + 1,
        'title': data['title'],
        'content': data['content']
    }
    notes.append(new_note)
    return jsonify({'message': 'Note added successfully'})
 
@app.route('/notes/<int:id>', methods=['GET'])
def get_note(id):
    for note in notes:
        if note['id'] == id:
            return jsonify(note)
    return jsonify({'message': 'Note not found'}), 404
 
@app.route('/notes/<int:id>', methods=['PUT'])
def update_note(id):
    data = request.get_json()
    for note in notes:
        if note['id'] == id:
            note.update({
                'title': data['title'],
                'content': data['content']
            })
            return jsonify({'message': 'Note updated successfully'})
    return jsonify({'message': 'Note not found'}), 404
 
@app.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    global notes
    notes = [note for note in notes if note['id'] != id]
    return jsonify({'message': 'Note deleted successfully'})
 
if __name__ == '__main__':
    app.run(debug=True, host="localhost",port="2200")
 
