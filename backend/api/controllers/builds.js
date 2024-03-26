module.exports = app => {
    const buildsDB = app.data.builds
    const controller = {}

    controller.listbuilds = (req, res) => res.status(200).json(buildsDB)
    controller.saveBuild = (req, res) => {
        data = {
            "nome": req.body.nome,
            "top1": req.body.top1,
            "top2": req.body.top2,
            "top3": req.body.top3,
            "armadura": req.body.armadura,
            "mao_esquerda": req.body.mao_esquerda,
            "mao_direita": req.body.mao_direita,
            "capa": req.body.capa,
            "sapato": req.body.sapato,
            "acessorio_1": req.body.acessorio_1,
            "acessorio_2": req.body.acessorio_2,
            "usuario": 1,
            "likes": 199
        }
        console.log("Build salva com sucesso!")
        res.status(201).json(data)
    }
    return controller
}