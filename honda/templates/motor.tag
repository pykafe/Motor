<motor>
    <div>Hau Nia Motor Sira</div>

    <ul>
        <li each={ motors }>
            Motor :{ model }<br />
            Fuel :{ fuel }<br />
            Size :{ engine_size }<br />
            <img src={ photo } width="200px" />
        </li>
    </ul>

    var self = this
    
    // a empy array of motors
    self.motors = []

    self.on('mount',function(){
        // get the list of motors from the api
        $.get('/api/motor/', function(data){
            self.motors = data.results
            self.update()
        })
    })
</motor>
