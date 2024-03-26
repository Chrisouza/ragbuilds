module.exports = app => {
    const controller = app.controllers.builds
    app.route('/api/v1/builds/')
    .get(controller.listbuilds)
    .post(controller.saveBuild)
}