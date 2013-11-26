var notesApp = angular.module('notesApp', []);

notesApp.config(function($routeProvider) {
    $routeProvider.
        when('/', {
            templateUrl: '/static/views/index.html',
            controller: 'NotesCtrl'
        }).
        otherwise({
            redirectTo: '/'
        });
});