const router = require('express').Router();
const User = require("../models/userModel");
const bycrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");

router.post("/singup", async (req,res)=>{
    try{
        const {email,password,phoneNumber,city} = req.body;

        // can use an email only one time
        const existingUser = await User.findOne({email:email})
        if(existingUser) return res.status(400).json({errorMessage:"An account with this email already exists !"})

        // hash the password
        const salt = await bycrypt.genSalt();
        const passwordHash = await bycrypt.hash(password,salt);

        // save a new user
        const newUser = new User({
            email,passwordHash,phoneNumber,city
        });
        const savedUser = await newUser.save();
        
        // make jwt and send it to front-end
        const token = jwt.sign({
            user:savedUser._id
        },process.env.JWT_SECRET)
        res.cookie("token",token,{
            httpOnly:true
        }).send()

    }catch(err){
        console.log(err);
        res.status(500).send();
    }
});


router.get("/login",async (req,res)=>{
    try{
        const {email,password} = req.body;

        // here i will check if email exist 
        const existingUser = await User.findOne({email})
        if(!existingUser) return res.status(400).json({errorMessage:"Wrong Email or Password !"})

        // here i will check if password correct
        const isPasswordCorrect = await bycrypt.compare(password , existingUser.passwordHash)
        if(!isPasswordCorrect) return res.status(400).json({errorMessage:"Wrong Email or Password !"})

        // here i will sign a token for the user
        const token = jwt.sign({
            user:existingUser._id
        },process.env.JWT_SECRET)
        res.cookie("token",token,{
            httpOnly:true
        }).status(200).send()
    }catch(err){
        res.json(err)
    }
})



module.exports = router