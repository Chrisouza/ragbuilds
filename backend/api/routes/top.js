module.exports = app => {
    const controller = app.controllers.top
    app.route('/api/v1/top/').get(controller.listtop)
}