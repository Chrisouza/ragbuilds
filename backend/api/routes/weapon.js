module.exports = app => {
    const controller = app.controllers.weapon
    app.route('/api/v1/weapons/').get(controller.listweapons)
}