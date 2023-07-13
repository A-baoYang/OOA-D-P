class Touch:
    def __init__(self, source: "MapObject", target: "MapObject") -> None:
        self._source = source
        self._target = target

    @property
    def source(self) -> "MapObject":
        return self._source

    @source.setter
    def source(self, source: "MapObject") -> None:
        self._source = source

    @property
    def target(self) -> "MapObject":
        return self._target

    @target.setter
    def target(self, target: "MapObject") -> None:
        self._target = target

    def _activate(self):
        if isinstance(self._target, "Teasure"):
            self._source.enter_state(state=self._target.touched_status_change)

        elif isinstance(self._target, "Obstacle"):
            
        elif isinstance(self._target, "Monster"):
            
