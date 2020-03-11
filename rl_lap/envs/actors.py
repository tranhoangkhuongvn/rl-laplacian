from . import env_base


class SingleActor:

    def __init__(self, env_factory):
        self._env = env_factory()
        self._time_step = self._env.reset()
        self._context = None

    def get_steps(self, n, policy_fn):
        steps = []
        for _ in range(n):
            state = (self._time_step, self._context)
            action, context = policy_fn(state)
            step = (self._time_step, action, self._context)
            steps.append(step)
            self._time_step = self._env.step(action)
            self._context = context
        return steps
