const mongoose = require("mongoose")

mongoose.connect('mongodb://localhost:27017/assignment5', {
    useNewUrlParser: true
})

const UserSchema = new mongoose.Schema({
    username: { type: String, unique: true },
    password: {
        type: String,
        set(val) {
            return require('bcryptjs').hashSync(val, 10)
        }
    },
})

const User = mongoose.model('User', UserSchema)
module.exports = { User }