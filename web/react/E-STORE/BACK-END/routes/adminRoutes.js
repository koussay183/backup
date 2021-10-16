const router = require('express').Router();
const User = require("../models/userModel");
const bycrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");

router.get("/login",(req,res)=>{
    try{
        console.log("from admin");
        res.send("from admin")
    }catch(e){
        res.json({err:e})
    }
})

module.exports = router