module.exports = app => {
    const topDB = app.data.top
    const controller = {}
    controller.listtop = (req, res) => res.status(200).json(topDB)
    return controller
}