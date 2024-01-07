const {User} = require('./models')
const express = require('express')
const path = require('path')
const jwt = require('jsonwebtoken')
const KEY = 'aaaa'

const app = express()
app.use(express.json())
app.use(express.static(path.join(__dirname, '')));

// ask for html
app.get('/', async(req, res) => {
    res.sendFile(path.join(__dirname, '/index.html'))
})

/*
app.get('/login.html', async (req, res) => {
    res.sendFile(path.join(__dirname, '/login.html'))
})

app.get('/register.html', async (req, res) => {
    res.sendFile(path.join(__dirname, '/register.html'))
})

app.get('/subpage/:subhtml', (req, res) => {
    res.sendFile(path.join(__dirname, '/subpage/' + req.params.subhtml))
})

app.get('/resource/img/thumbnail/:img', (req, res) => {
    res.sendFile(path.join(__dirname, '/resource/img/thumbnail/' + req.params.img))
})

*/

app.get('/api/users', async (req, res) => {
    const users = await User.find()
    res.send(users)
})

app.post('/api/register', async(req, res) => {
    var emailRegex = /^\w+((.\w+)|(-\w+))@[A-Za-z0-9]+((.|-)[A-Za-z0-9]+).[A-Za-z0-9]+$/;
    var email = req.body.username;
    var password = req.body.password;

    if (email === "") {
        return res.status(422).send(
            '邮箱不可为空。'
        )
    }
    if (!emailRegex.test(email)) {
        return res.status(422).send(
            '请输入合法邮箱。'
        )
    }

    if (password === "") {
        return res.status(422).send(
            '密码不可为空。'
        )
    }
    let hardPassword = new RegExp('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{8,})');

    if (!hardPassword.test(password)) {
        return res.status(422).send(
            "密码过于简单，请用一个更复杂的密码。密码应符合下面要求：1、至少8个字符；2、至少一个小写字母；3、至少一个大写字母；4、至少一个数字；5、至少一个特殊字符。"
        )
    }

    const oldUser = await User.findOne({
        username:req.body.username
    })
    if (oldUser) {
        return res.status(422).send(
            '邮箱已被注册'
        )
    }

    const user = await User.create({
        username: req.body.username,
        password: req.body.password,
    })
    res.send("注册成功！请前往登录页登录")
})

app.post('/api/login', async (req, res) => {
    const user = await User.findOne({
        username:req.body.username
    })
    if (!user) {
        return res.status(422).send(
            '邮箱不存在'
        )
    }
    const isPasswordValid = require('bcryptjs').compareSync(
        req.body.password,
        user.password
    )
    if (!isPasswordValid) {
        return res.status(422).send(
            '密码无效'
        )
    }
    // Valid. Generate token.

    const token = jwt.sign({
        id: String(user._id),
    }, KEY)

    res.send({
        token
    })
})

const auth = async (req, res, next) => {
    const raw = String(req.headers.authorization).split(' ').pop()
    const {id} = jwt.verify(raw, KEY)
    req.user = await User.findById(id)
    next()
}

app.get('/api/profile', auth, async (req, res) => {
    res.send(req.user)
})

app.listen(3001, () => {
    console.log('http:localhost:3001')
})