const { exec } = require("child_process");
const express = require('express')
const app = express()
const cors = require('cors')
const bodyParser = require('body-parser')

const execPromise = (str,input="")=>{
    return new Promise((resolve,reject)=>{
        const child = exec(str,{
            cwd: process.cwd()
          }, (error, stdout, stderr) => {
            if (error) {
                reject(error)
                return;
            }
            resolve(stdout)
        });
        if(input)child.stdin.write(input + '\n')
    })
}

app.use(cors())
app.use(bodyParser.json())

app.post('/compile',async (req,res)=>{
    const body = req.body
    console.log(body)
    const compileRes= await execPromise(`python parser.py tests/${body.exampleKey}.c output.ll`)
    res.json({
        compileRes:compileRes
    })
})

app.post('/run',async (req,res)=>{
    const body = req.body
    const runRes = await execPromise(`lli output.ll`,body.input)
    res.json({
        runRes:runRes
    })
})

app.listen(5000,()=>{
    console.log("Listening at 5000")
})