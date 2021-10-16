const express = require('express');
const app = express();
const mongoose = require('mongoose')
const dotenv = require('dotenv')
const cors = require('cors')

const PORT = process.env.PORT || 5000
dotenv.config()
app.use(express.json())
app.use(cors())

// Connect To Data Base
mongoose.connect(
    process.env.MONGO_CONNECT,
    { useNewUrlParser: true , useUnifiedTopology: true },
    ()=>{
        // Listening
        app.listen(PORT);
        console.log(`Server Listening On Port ${PORT}`);
        console.log("Connected to DB!");
    }
);

// Set Up  Routes
app.use("/user",require('./routes/userRoutes'))
app.use("/admin",require("./routes/adminRoutes"))