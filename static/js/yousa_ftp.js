var app = new Vue({
    el: "#app",
    data: {
        pathList: [],
        dirList: [],
        fileList: []
    },
    mounted: function () {
        this.GetList('');
    },
    computed: {
        path: function () {
            return this.pathList.join('/')
        },
        backPath: function () {
            return this.pathList.slice(0, -1).join('/')
        },
        isHome: function () {
            this.pathList.length == 1 ? true : false

        }
    },
    methods: {

        GetLast: function () {
            axios.post('/api/v3/ftp', {
                    path: this.backPath
                })
                .then(function (response) {
                    this.dirList = response.data.dirList
                    this.fileList = response.data.fileList
                    this.pathList.pop()

                }.bind(this))
        },
        GetList: function (nextPath) {
            axios.post('/api/v3/ftp', {
                    path: this.path + '/' + nextPath
                })
                .then(function (response) {
                    this.dirList = response.data.dirList
                    this.fileList = response.data.fileList
                    this.pathList.push(nextPath)

                }.bind(this))
        },
        GetFtpPath: function (name) {
            return 'ftp://' + window.location.host + this.path + '/' + name
        }
    }
})