import json
import os
import math

# File paths
DART_FILE = r'lib/services/seed_data.dart'
JSON_FILE = r'scratch/seed_data.json'

def make_conceptual_pool(chapter_idx):
    """
    Returns a pool of distinct, high-quality English conceptual questions for a given chapter.
    We define 15-20 conceptual questions for each of the 11 chapters.
    """
    pool = []
    
    if chapter_idx == 1:  # Oscillatory Motion
        pool = [
            {"question": "What is oscillatory motion?", "options": {"a": "Movement in a straight line with constant acceleration", "b": "To-and-fro or back-and-forth periodic motion about an equilibrium position", "c": "Rotational motion around a fixed axis", "d": "Random motion in three dimensions"}, "correctAnswer": "b"},
            {"question": "In simple harmonic motion, where is the velocity of the oscillating particle maximum?", "options": {"a": "At the maximum displacement", "b": "At the equilibrium position", "c": "At half the amplitude", "d": "It remains constant everywhere"}, "correctAnswer": "b"},
            {"question": "When an oscillator reaches its maximum displacement, its acceleration is:", "options": {"a": "Zero", "b": "Maximum", "c": "Constant and negative", "d": "Dependent on the mass only"}, "correctAnswer": "b"},
            {"question": "What does the amplitude of an oscillation represent?", "options": {"a": "The time taken for one complete cycle", "b": "The maximum displacement from the equilibrium position", "c": "The number of cycles per second", "d": "The total energy of the system"}, "correctAnswer": "b"},
            {"question": "What is the relationship between frequency (f) and period (T)?", "options": {"a": "They are directly proportional (f = T)", "b": "They are inversely related (f = 1/T)", "c": "They are independent of each other", "d": "f = 2 * pi * T"}, "correctAnswer": "b"},
            {"question": "The SI unit of frequency is:", "options": {"a": "Second (s)", "b": "Hertz (Hz)", "c": "Newton (N)", "d": "Meter (m)"}, "correctAnswer": "b"},
            {"question": "Hooke's Law states that the restoring force of a spring is directly proportional to:", "options": {"a": "The square of the displacement", "b": "The displacement, and acts in the opposite direction", "c": "The mass of the attached object", "d": "The velocity of the oscillation"}, "correctAnswer": "b"},
            {"question": "If the length of a simple pendulum is quadrupled, what happens to its period?", "options": {"a": "It is doubled", "b": "It is halved", "c": "It remains the same", "d": "It is quadrupled"}, "correctAnswer": "a"},
            {"question": "The period of a simple pendulum is independent of:", "options": {"a": "The length of the string", "b": "The mass of the pendulum bob", "c": "The acceleration due to gravity", "d": "The location of the pendulum"}, "correctAnswer": "b"},
            {"question": "At the equilibrium position, the kinetic energy of a simple harmonic oscillator is:", "options": {"a": "Zero", "b": "Maximum", "c": "Equal to the potential energy", "d": "Negative"}, "correctAnswer": "b"},
            {"question": "At maximum displacement, the total energy of a simple harmonic oscillator is:", "options": {"a": "Entirely kinetic energy", "b": "Entirely potential energy", "c": "Half kinetic and half potential energy", "d": "Zero"}, "correctAnswer": "b"},
            {"question": "What is the phase difference between displacement and velocity in simple harmonic motion?", "options": {"a": "0 degrees", "b": "90 degrees (pi/2 rad)", "c": "180 degrees (pi rad)", "d": "270 degrees (3*pi/2 rad)"}, "correctAnswer": "b"},
            {"question": "If the amplitude of a simple harmonic oscillator is doubled, the total mechanical energy is:", "options": {"a": "Doubled", "b": "Halved", "c": "Four times greater", "d": "Unchanged"}, "correctAnswer": "c"},
            {"question": "Which of the following is an example of simple harmonic motion?", "options": {"a": "A bouncing ball on a hard floor", "b": "The motion of a simple pendulum with a small angle of swing", "c": "The rotation of the Earth on its axis", "d": "The motion of a car moving at a constant speed around a circular track"}, "correctAnswer": "b"},
            {"question": "What happens to the period of a mass-spring system if the mass is doubled?", "options": {"a": "It decreases by a factor of 2", "b": "It increases by a factor of square root of 2", "c": "It doubles", "d": "It remains unchanged"}, "correctAnswer": "b"}
        ]
        
    elif chapter_idx == 2:  # Wave Motion
        pool = [
            {"question": "What is a wave in physics?", "options": {"a": "The physical transport of matter over a long distance", "b": "A disturbance that transfers energy through a medium or space without transferring matter", "c": "A mechanical force applied to a solid boundary", "d": "The reflection of sound in an enclosed space"}, "correctAnswer": "b"},
            {"question": "Waves that require a material medium to propagate are called:", "options": {"a": "Electromagnetic waves", "b": "Mechanical waves", "c": "Matter waves", "d": "Transverse waves"}, "correctAnswer": "b"},
            {"question": "In which type of wave do particles of the medium vibrate parallel to the direction of wave propagation?", "options": {"a": "Transverse waves", "b": "Longitudinal waves", "c": "Surface waves", "d": "Electromagnetic waves"}, "correctAnswer": "b"},
            {"question": "In which type of wave do particles of the medium vibrate perpendicular to the direction of wave propagation?", "options": {"a": "Longitudinal waves", "b": "Transverse waves", "c": "Sound waves", "d": "Seismic P-waves"}, "correctAnswer": "b"},
            {"question": "What is the definition of wavelength?", "options": {"a": "The maximum distance a wave travels in one minute", "b": "The distance between two consecutive points in phase, such as two crests or two troughs", "c": "The height of the wave crest from the center line", "d": "The time taken for a wave to travel one meter"}, "correctAnswer": "b"},
            {"question": "Which of the following wave properties remains unchanged when a wave passes from one medium to another?", "options": {"a": "Wavelength", "b": "Velocity", "c": "Frequency", "d": "Amplitude"}, "correctAnswer": "c"},
            {"question": "What is the formula relating wave velocity (v), frequency (f), and wavelength (lambda)?", "options": {"a": "v = f / lambda", "b": "v = f * lambda", "c": "v = lambda / f", "d": "v = f + lambda"}, "correctAnswer": "b"},
            {"question": "Which of the following waves is an example of an electromagnetic wave?", "options": {"a": "Sound wave in air", "b": "Water wave on a pond", "c": "Radio wave", "d": "Wave on a stretched string"}, "correctAnswer": "c"},
            {"question": "The distance from the equilibrium line to the crest of a transverse wave is called:", "options": {"a": "Wavelength", "b": "Period", "c": "Amplitude", "d": "Frequency"}, "correctAnswer": "c"},
            {"question": "Which wave phenomenon occurs when a wave bends around the edge of an obstacle or spreads through a narrow opening?", "options": {"a": "Reflection", "b": "Refraction", "c": "Diffraction", "d": "Interference"}, "correctAnswer": "c"},
            {"question": "What happens when two wave crests overlap to produce a larger wave?", "options": {"a": "Destructive interference occurs", "b": "Constructive interference occurs", "c": "The waves cancel each other out", "d": "Refraction occurs"}, "correctAnswer": "b"},
            {"question": "Electromagnetic waves can travel through:", "options": {"a": "Solids and liquids only", "b": "Gases and plasmas only", "c": "A vacuum as well as material media", "d": "Perfect conductors only"}, "correctAnswer": "c"},
            {"question": "The time taken for one complete wave cycle to pass a given point is called the:", "options": {"a": "Frequency", "b": "Wavelength", "c": "Period", "d": "Amplitude"}, "correctAnswer": "c"},
            {"question": "A sound wave is a:", "options": {"a": "Transverse electromagnetic wave", "b": "Longitudinal mechanical wave", "c": "Transverse mechanical wave", "d": "Longitudinal electromagnetic wave"}, "correctAnswer": "b"},
            {"question": "The wave property that is directly related to the energy carried by a wave is:", "options": {"a": "Wavelength", "b": "Velocity", "c": "Amplitude", "d": "Frequency"}, "correctAnswer": "c"}
        ]
        
    elif chapter_idx == 3:  # Sound Waves
        pool = [
            {"question": "Sound waves cannot travel through:", "options": {"a": "Water", "b": "Steel", "c": "A vacuum", "d": "Air"}, "correctAnswer": "c"},
            {"question": "In which of the following media does sound travel fastest?", "options": {"a": "Gases (like air)", "b": "Liquids (like water)", "c": "Solids (like iron)", "d": "It travels at the same speed in all media"}, "correctAnswer": "c"},
            {"question": "The pitch of a sound wave is determined primarily by its:", "options": {"a": "Amplitude", "b": "Frequency", "c": "Velocity", "d": "Wavelength"}, "correctAnswer": "b"},
            {"question": "The normal range of hearing for a healthy young human is:", "options": {"a": "0 Hz to 20 Hz", "b": "20 Hz to 20,000 Hz", "c": "20,000 Hz to 2 MHz", "d": "100 Hz to 10,000 Hz"}, "correctAnswer": "b"},
            {"question": "What is the phenomenon where a sound wave reflects off a hard surface and is heard again after a delay?", "options": {"a": "Resonance", "b": "Echo", "c": "Doppler effect", "d": "Refraction"}, "correctAnswer": "b"},
            {"question": "The Doppler effect is observed as an apparent change in frequency due to:", "options": {"a": "The medium through which the sound travels changing temperature", "b": "Relative motion between the sound source and the observer", "c": "The absorption of sound waves by the environment", "d": "Two sound waves of different amplitudes interfering"}, "correctAnswer": "b"},
            {"question": "What is the beat frequency produced when two sound waves of frequencies 256 Hz and 260 Hz are sounded together?", "options": {"a": "516 Hz", "b": "4 Hz", "c": "2 Hz", "d": "258 Hz"}, "correctAnswer": "b"},
            {"question": "The loudness of a sound is related to which wave property?", "options": {"a": "Frequency", "b": "Amplitude", "c": "Wavelength", "d": "Wave speed"}, "correctAnswer": "b"},
            {"question": "What occurs when the frequency of a forced vibration matches the natural frequency of an object, leading to a large amplitude of vibration?", "options": {"a": "Diffraction", "b": "Resonance", "c": "Damping", "d": "Beats"}, "correctAnswer": "b"},
            {"question": "A sound wave of frequency less than 20 Hz is classified as:", "options": {"a": "Ultrasonic", "b": "Infrasonic", "c": "Audible", "d": "Supersonic"}, "correctAnswer": "b"},
            {"question": "A sound wave of frequency greater than 20,000 Hz is classified as:", "options": {"a": "Infrasonic", "b": "Ultrasonic", "c": "Audible", "d": "Subsonic"}, "correctAnswer": "b"},
            {"question": "The quality or timbre of a sound depends on:", "options": {"a": "The frequency only", "b": "The speed of propagation only", "c": "The number and relative intensity of overtones/harmonics present", "d": "The amplitude only"}, "correctAnswer": "c"},
            {"question": "What kind of boundary condition exists at the open end of an air column or organ pipe?", "options": {"a": "Displacement node", "b": "Displacement antinode", "c": "Pressure antinode", "d": "A fixed boundary"}, "correctAnswer": "b"},
            {"question": "In a closed organ pipe (closed at one end), the harmonics produced are:", "options": {"a": "All integer multiples of the fundamental frequency", "b": "Odd harmonics only", "c": "Even harmonics only", "d": "None of the above"}, "correctAnswer": "b"},
            {"question": "What is the fundamental wavelength of a pipe of length L open at both ends?", "options": {"a": "L/2", "b": "L", "c": "2L", "d": "4L"}, "correctAnswer": "c"}
        ]
        
    elif chapter_idx == 4:  # Reflection of Light
        pool = [
            {"question": "According to the law of reflection, the angle of incidence is:", "options": {"a": "Greater than the angle of reflection", "b": "Equal to the angle of reflection", "c": "Less than the angle of reflection", "d": "Independent of the angle of reflection"}, "correctAnswer": "b"},
            {"question": "The image formed by a plane mirror is always:", "options": {"a": "Real, inverted, and magnified", "b": "Virtual, erect, and the same size as the object", "c": "Real, erect, and diminished", "d": "Virtual, inverted, and diminished"}, "correctAnswer": "b"},
            {"question": "A spherical mirror with its reflecting surface curved inwards is called a:", "options": {"a": "Convex mirror", "b": "Concave mirror", "c": "Plane mirror", "d": "Parabolic mirror"}, "correctAnswer": "b"},
            {"question": "A spherical mirror with its reflecting surface curved outwards is called a:", "options": {"a": "Concave mirror", "b": "Convex mirror", "c": "Cylindrical mirror", "d": "Bifocal mirror"}, "correctAnswer": "b"},
            {"question": "The relation between the focal length (f) and the radius of curvature (R) of a spherical mirror is:", "options": {"a": "f = 2 * R", "b": "f = R / 2", "c": "f = R", "d": "f = R^2"}, "correctAnswer": "b"},
            {"question": "Which mirror is commonly used as a rear-view mirror in vehicles because it provides a wide field of view?", "options": {"a": "Concave mirror", "b": "Convex mirror", "c": "Plane mirror", "d": "Double convex mirror"}, "correctAnswer": "b"},
            {"question": "What type of image is formed when light rays actually meet at a point after reflection?", "options": {"a": "Virtual image", "b": "Real image", "c": "Magnified virtual image", "d": "Erect image"}, "correctAnswer": "b"},
            {"question": "The magnification (m) of a mirror is given by the formula:", "options": {"a": "m = -di / do", "b": "m = di / do", "c": "m = do / di", "d": "m = -do / di"}, "correctAnswer": "a"},
            {"question": "If the magnification of a mirror is negative, it indicates that the image is:", "options": {"a": "Virtual and erect", "b": "Real and inverted", "c": "Virtual and inverted", "d": "Real and erect"}, "correctAnswer": "b"},
            {"question": "For a convex mirror, the focal length is considered:", "options": {"a": "Positive", "b": "Negative", "c": "Zero", "d": "Variable depending on object distance"}, "correctAnswer": "b"},
            {"question": "What kind of mirror is used by dentists to see large images of teeth?", "options": {"a": "Convex mirror", "b": "Concave mirror", "c": "Plane mirror", "d": "Cylindrical mirror"}, "correctAnswer": "b"},
            {"question": "Where must an object be placed in front of a concave mirror so that its image is real, inverted, and the same size?", "options": {"a": "At the focal point (F)", "b": "At the center of curvature (C)", "c": "Between F and C", "d": "Beyond the center of curvature"}, "correctAnswer": "b"},
            {"question": "If an object is placed at the principal focus of a concave mirror, where is the image formed?", "options": {"a": "At the center of curvature", "b": "At infinity", "c": "Between the focus and the pole", "d": "Behind the mirror"}, "correctAnswer": "b"},
            {"question": "A virtual image cannot be:", "options": {"a": "Photographed", "b": "Projected onto a screen", "c": "Seen by the eye", "d": "Formed by reflection"}, "correctAnswer": "b"},
            {"question": "What is the principal axis of a spherical mirror?", "options": {"a": "The line passing through the focal point only", "b": "The straight line passing through the center of curvature and the pole of the mirror", "c": "The line tangent to the mirror surface at its edge", "d": "The normal at any point of incidence"}, "correctAnswer": "b"}
        ]
        
    elif chapter_idx == 5:  # Refraction of Light
        pool = [
            {"question": "What causes the refraction of light when it passes from one medium to another?", "options": {"a": "A change in the color of the light", "b": "A change in the speed of light in different media", "c": "The absorption of light by the second medium", "d": "The reflection of light at the boundary"}, "correctAnswer": "b"},
            {"question": "When a ray of light passes from a less dense medium (like air) to a denser medium (like glass), it bends:", "options": {"a": "Away from the normal", "b": "Towards the normal", "c": "Along the boundary line", "d": "It does not bend at all"}, "correctAnswer": "b"},
            {"question": "What is the formula for the refractive index of a medium (n) in terms of the speed of light?", "options": {"a": "n = v / c", "b": "n = c / v", "c": "n = c * v", "d": "n = 1 / (c * v)"}, "correctAnswer": "b"},
            {"question": "According to Snell's Law, for two given media:", "options": {"a": "n1 * sin(theta2) = n2 * sin(theta1)", "b": "n1 * sin(theta1) = n2 * sin(theta2)", "c": "sin(theta1) / sin(theta2) = n2 / n1", "d": "n1 * n2 = sin(theta1) * sin(theta2)"}, "correctAnswer": "b"},
            {"question": "A lens that is thicker in the middle than at the edges is called a:", "options": {"a": "Concave lens (diverging)", "b": "Convex lens (converging)", "c": "Cylindrical lens", "d": "Plano-concave lens"}, "correctAnswer": "b"},
            {"question": "A lens that is thinner in the middle than at the edges is called a:", "options": {"a": "Convex lens", "b": "Concave lens", "c": "Biconvex lens", "d": "Cylindrical lens"}, "correctAnswer": "b"},
            {"question": "The power of a lens (P) is related to its focal length (f) in meters by:", "options": {"a": "P = f", "b": "P = 1 / f", "c": "P = 1 / f^2", "d": "P = 100 * f"}, "correctAnswer": "b"},
            {"question": "The SI unit of the power of a lens is:", "options": {"a": "Meter (m)", "b": "Dioptre (D)", "c": "Watt (W)", "d": "Joule (J)"}, "correctAnswer": "b"},
            {"question": "A convex lens is also known as a:", "options": {"a": "Diverging lens", "b": "Converging lens", "c": "Plane lens", "d": "Biconcave lens"}, "correctAnswer": "b"},
            {"question": "A concave lens is also known as a:", "options": {"a": "Converging lens", "b": "Diverging lens", "c": "Plane lens", "d": "Biconvex lens"}, "correctAnswer": "b"},
            {"question": "If a lens has a focal length of +0.5 meters, what is its power?", "options": {"a": "-2.0 D", "b": "+2.0 D", "c": "+0.5 D", "d": "+1.0 D"}, "correctAnswer": "b"},
            {"question": "What is the nature of the image formed by a concave lens for a real object?", "options": {"a": "Always real, inverted, and magnified", "b": "Always virtual, erect, and diminished", "c": "Real, erect, and of the same size", "d": "Dependent on the object position"}, "correctAnswer": "b"},
            {"question": "For a thin lens, the lens formula is:", "options": {"a": "1/f = 1/do - 1/di", "b": "1/f = 1/do + 1/di", "c": "1/f = 1/di - 1/do", "d": "f = do + di"}, "correctAnswer": "b"},
            {"question": "When light travels from glass to air, the angle of refraction is:", "options": {"a": "Equal to the angle of incidence", "b": "Greater than the angle of incidence", "c": "Less than the angle of incidence", "d": "Exactly 90 degrees"}, "correctAnswer": "b"},
            {"question": "Which of the following values can NEVER be the refractive index of a material medium?", "options": {"a": "1.33", "b": "0.85", "c": "1.52", "d": "2.42"}, "correctAnswer": "b"}
        ]
        
    elif chapter_idx == 6:  # Dispersion of Light
        pool = [
            {"question": "What is the dispersion of light?", "options": {"a": "The scattering of light by dust particles", "b": "The splitting of white light into its component colors when passing through a prism", "c": "The absorption of specific wavelengths of light by a medium", "d": "The reflection of light off a rough surface"}, "correctAnswer": "b"},
            {"question": "Which color of light bends the least when white light passes through a glass prism?", "options": {"a": "Violet", "b": "Red", "c": "Green", "d": "Yellow"}, "correctAnswer": "b"},
            {"question": "Which color of light bends the most when white light passes through a glass prism?", "options": {"a": "Red", "b": "Violet", "c": "Blue", "d": "Orange"}, "correctAnswer": "b"},
            {"question": "What is the critical angle?", "options": {"a": "The angle of incidence for which the angle of refraction is 90 degrees", "b": "The angle of reflection for a plane mirror", "c": "The maximum angle of deviation through a prism", "d": "The angle at which light is completely absorbed by a medium"}, "correctAnswer": "a"},
            {"question": "What are the two conditions required for total internal reflection to occur?", "options": {"a": "Light must travel from a less dense to a denser medium, and angle of incidence must be less than critical angle", "b": "Light must travel from a denser to a less dense medium, and angle of incidence must be greater than critical angle", "c": "Light must hit a perfectly reflective metal mirror at a 45-degree angle", "d": "Light must be monochromatic and pass through a single slit"}, "correctAnswer": "b"},
            {"question": "Which of the following optical instruments works on the principle of total internal reflection?", "options": {"a": "Simple magnifying glass", "b": "Optical fiber", "c": "Astronomical telescope", "d": "Compound microscope"}, "correctAnswer": "b"},
            {"question": "The band of seven colors produced due to dispersion of white light is called a:", "options": {"a": "Reflection pattern", "b": "Spectrum", "c": "Diffraction grating", "d": "Hologram"}, "correctAnswer": "b"},
            {"question": "Why does dispersion occur in a glass prism?", "options": {"a": "Because different colors of light travel at different speeds in glass", "b": "Because the prism absorbs all colors except red and violet", "c": "Because of interference between light waves at the boundaries", "d": "Because the density of the glass is different at the top and bottom"}, "correctAnswer": "a"},
            {"question": "The refractive index of glass is greatest for which of the following colors of light?", "options": {"a": "Red", "b": "Violet", "c": "Yellow", "d": "Green"}, "correctAnswer": "b"},
            {"question": "The critical angle (theta_c) for a medium is related to its refractive index (n) relative to air by:", "options": {"a": "sin(theta_c) = n", "b": "sin(theta_c) = 1 / n", "c": "cos(theta_c) = 1 / n", "d": "tan(theta_c) = n"}, "correctAnswer": "b"},
            {"question": "A rainbow is formed due to a combination of which light phenomena?", "options": {"a": "Reflection and refraction only", "b": "Refraction, dispersion, and total internal reflection within water droplets", "c": "Interference and diffraction of sunlight", "d": "Absorption and scattering of light by air molecules"}, "correctAnswer": "b"},
            {"question": "Which color of white light has the highest frequency?", "options": {"a": "Red", "b": "Violet", "c": "Blue", "d": "Green"}, "correctAnswer": "b"},
            {"question": "In optical fibers, the core is surrounded by a layer of lower refractive index material called the:", "options": {"a": "Cladding", "b": "Sheath", "c": "Jacket", "d": "Shield"}, "correctAnswer": "a"},
            {"question": "Which color of white light has the longest wavelength in vacuum?", "options": {"a": "Violet", "b": "Red", "c": "Yellow", "d": "Blue"}, "correctAnswer": "b"},
            {"question": "When light passes through a rectangular glass block, what happens to the emergent ray relative to the incident ray?", "options": {"a": "It is perpendicular to the incident ray", "b": "It is parallel to the incident ray but laterally displaced", "c": "It is completely absorbed", "d": "It returns along the incident path"}, "correctAnswer": "b"}
        ]
        
    elif chapter_idx == 7:  # Electromagnetic Induction
        pool = [
            {"question": "What is electromagnetic induction?", "options": {"a": "The production of magnetism by an electric current", "b": "The production of an electromotive force (emf) across a conductor exposed to a time-varying magnetic flux", "c": "The alignment of magnetic domains in a ferromagnetic material", "d": "The discharge of electricity through a gas"}, "correctAnswer": "b"},
            {"question": "Faraday's Law of induction states that the induced emf in a closed circuit is directly proportional to:", "options": {"a": "The constant strength of the magnetic field", "b": "The time rate of change of magnetic flux through the circuit", "c": "The electrical resistance of the wire", "d": "The length of the conductor only"}, "correctAnswer": "b"},
            {"question": "Lenz's Law states that the direction of the induced current is such that it:", "options": {"a": "Supports the change in magnetic flux that produced it", "b": "Opposes the change in magnetic flux that produced it", "c": "Is always perpendicular to the conductor's velocity", "d": "Points from north to south poles of the magnet"}, "correctAnswer": "b"},
            {"question": "Lenz's Law is a consequence of the law of conservation of:", "options": {"a": "Charge", "b": "Energy", "c": "Momentum", "d": "Mass"}, "correctAnswer": "b"},
            {"question": "The SI unit of magnetic flux is the:", "options": {"a": "Tesla (T)", "b": "Weber (Wb)", "c": "Henry (H)", "d": "Volt (V)"}, "correctAnswer": "b"},
            {"question": "The SI unit of self-inductance is the:", "options": {"a": "Farad (F)", "b": "Henry (H)", "c": "Ohm", "d": "Tesla"}, "correctAnswer": "b"},
            {"question": "An electrical generator is a device that converts:", "options": {"a": "Electrical energy into mechanical energy", "b": "Mechanical energy into electrical energy", "c": "Chemical energy into electrical energy", "d": "Heat energy into electrical energy"}, "correctAnswer": "b"},
            {"question": "What is the function of a transformer?", "options": {"a": "To convert alternating current into direct current", "b": "To increase or decrease the voltage of alternating current", "c": "To generate mechanical energy from magnetic fields", "d": "To store electric charge"}, "correctAnswer": "b"},
            {"question": "In a step-up transformer, the number of turns in the secondary coil (Ns) is:", "options": {"a": "Less than in the primary coil (Np)", "b": "Greater than in the primary coil (Np)", "c": "Equal to that in the primary coil (Np)", "d": "Zero"}, "correctAnswer": "b"},
            {"question": "A transformer works on the principle of:", "options": {"a": "Self-induction", "b": "Mutual induction", "c": "The photoelectric effect", "d": "Electrostatic shielding"}, "correctAnswer": "b"},
            {"question": "Why are transformer cores laminated?", "options": {"a": "To reduce copper resistance losses", "b": "To minimize energy losses due to eddy currents", "c": "To increase the magnetic permeability of the core", "d": "To prevent electric shock to operators"}, "correctAnswer": "b"},
            {"question": "What type of current is required for a transformer to operate continuously?", "options": {"a": "Constant Direct Current (DC)", "b": "Alternating Current (AC)", "c": "Pulsating DC only", "d": "Transient electrostatic current"}, "correctAnswer": "b"},
            {"question": "The formula for magnetic flux (Phi) through a flat area A in a uniform magnetic field B is:", "options": {"a": "Phi = B / A", "b": "Phi = B * A * cos(theta)", "c": "Phi = B * A * sin(theta)", "d": "Phi = B^2 * A"}, "correctAnswer": "b"},
            {"question": "What is the induced emf in a straight conductor of length L moving with speed v perpendicular to a uniform magnetic field B?", "options": {"a": "e = B / (L * v)", "b": "e = B * L * v", "c": "e = B * L / v", "d": "e = B * v / L"}, "correctAnswer": "b"},
            {"question": "If a permanent magnet is held stationary inside a coil of wire, the induced emf in the coil is:", "options": {"a": "Constant and high", "b": "Zero", "c": "Alternating periodically", "d": "Proportional to the number of turns"}, "correctAnswer": "b"}
        ]
        
    elif chapter_idx == 8:  # Alternating Current
        pool = [
            {"question": "What is alternating current (AC)?", "options": {"a": "Current that flows in one direction only with constant magnitude", "b": "Current that periodically reverses direction and changes its magnitude continuously with time", "c": "Current that flows only through semiconductors", "d": "Current generated by chemical batteries"}, "correctAnswer": "b"},
            {"question": "What is the relationship between the peak voltage (V0) and the root-mean-square voltage (Vrms) in an AC circuit?", "options": {"a": "Vrms = V0 * sqrt(2)", "b": "Vrms = V0 / sqrt(2)", "c": "Vrms = V0 / 2", "d": "Vrms = V0 * 2"}, "correctAnswer": "b"},
            {"question": "The inductive reactance (XL) of an inductor in an AC circuit is given by:", "options": {"a": "XL = 1 / (2 * pi * f * L)", "b": "XL = 2 * pi * f * L", "c": "XL = 2 * pi * f / L", "d": "XL = L / (2 * pi * f)"}, "correctAnswer": "b"},
            {"question": "The capacitive reactance (XC) of a capacitor in an AC circuit is given by:", "options": {"a": "XC = 2 * pi * f * C", "b": "XC = 1 / (2 * pi * f * C)", "c": "XC = 2 * pi * f / C", "d": "XC = C / (2 * pi * f)"}, "correctAnswer": "b"},
            {"question": "How does capacitive reactance change as the frequency of the AC source increases?", "options": {"a": "It increases linearly", "b": "It decreases", "c": "It remains unchanged", "d": "It drops to zero instantly"}, "correctAnswer": "b"},
            {"question": "How does inductive reactance change as the frequency of the AC source increases?", "options": {"a": "It decreases", "b": "It increases linearly", "c": "It remains unchanged", "d": "It is inversely proportional to frequency"}, "correctAnswer": "b"},
            {"question": "The total opposition to current flow in a series RLC alternating current circuit is called:", "options": {"a": "Resistance", "b": "Impedance (Z)", "c": "Reactance", "d": "Admittance"}, "correctAnswer": "b"},
            {"question": "What is the phase difference between voltage and current in a purely resistive AC circuit?", "options": {"a": "90 degrees", "b": "0 degrees (in phase)", "c": "180 degrees", "d": "270 degrees"}, "correctAnswer": "b"},
            {"question": "In a purely inductive AC circuit, the current:", "options": {"a": "Leads the voltage by 90 degrees", "b": "Lags the voltage by 90 degrees", "c": "Is in phase with the voltage", "d": "Lags the voltage by 180 degrees"}, "correctAnswer": "b"},
            {"question": "In a purely capacitive AC circuit, the current:", "options": {"a": "Lags the voltage by 90 degrees", "b": "Leads the voltage by 90 degrees", "c": "Is in phase with the voltage", "d": "Leads the voltage by 180 degrees"}, "correctAnswer": "b"},
            {"question": "What is the condition for resonance in a series RLC AC circuit?", "options": {"a": "XL = R", "b": "XL = XC", "c": "XC = R", "d": "XL = XC = R"}, "correctAnswer": "b"},
            {"question": "What is the resonant frequency (f0) of a series RLC circuit?", "options": {"a": "f0 = 2 * pi * sqrt(L * C)", "b": "f0 = 1 / (2 * pi * sqrt(L * C))", "c": "f0 = sqrt(L * C) / (2 * pi)", "d": "f0 = 1 / (sqrt(L * C))"}, "correctAnswer": "b"},
            {"question": "The power factor of an AC circuit is defined as:", "options": {"a": "sin(theta)", "b": "cos(theta)", "c": "tan(theta)", "d": "R / Z^2"}, "correctAnswer": "b"},
            {"question": "What is the power dissipated in a purely capacitive or purely inductive AC circuit?", "options": {"a": "Maximum", "b": "Zero", "c": "Vrms * Irms", "d": "Irms^2 * XC"}, "correctAnswer": "b"},
            {"question": "The frequency of domestic AC electricity in most countries is typically:", "options": {"a": "12 V", "b": "50 Hz or 60 Hz", "c": "220 Hz", "d": "1000 Hz"}, "correctAnswer": "b"}
        ]
        
    elif chapter_idx == 9:  # Electronics
        pool = [
            {"question": "Which of the following describes a semiconductor?", "options": {"a": "A material that conducts electricity extremely well at all temperatures", "b": "A material whose electrical conductivity lies between that of a conductor and an insulator", "c": "A material that completely blocks current at all temperatures", "d": "A material that conducts electricity only under magnetic exposure"}, "correctAnswer": "b"},
            {"question": "The process of adding a controlled amount of impurity to an intrinsic semiconductor to change its conductivity is called:", "options": {"a": "Ionization", "b": "Doping", "c": "Rectification", "d": "Amplification"}, "correctAnswer": "b"},
            {"question": "An n-type semiconductor is created by doping a pure semiconductor with:", "options": {"a": "Trivalent impurities (like Boron)", "b": "Pentavalent impurities (like Phosphorus)", "c": "Monovalent impurities", "d": "Noble gases"}, "correctAnswer": "b"},
            {"question": "A p-type semiconductor is created by doping a pure semiconductor with:", "options": {"a": "Pentavalent impurities", "b": "Trivalent impurities", "c": "Hexavalent impurities", "d": "Pure carbon"}, "correctAnswer": "b"},
            {"question": "In an n-type semiconductor, the majority charge carriers are:", "options": {"a": "Holes", "b": "Electrons", "c": "Protons", "d": "Positrons"}, "correctAnswer": "b"},
            {"question": "In a p-type semiconductor, the majority charge carriers are:", "options": {"a": "Electrons", "b": "Holes", "c": "Protons", "d": "Neutrons"}, "correctAnswer": "b"},
            {"question": "A p-n junction diode is a device that allows electric current to flow:", "options": {"a": "In both directions equally", "b": "Mainly in one direction (forward bias)", "c": "Only when reverse biased", "d": "Only at absolute zero"}, "correctAnswer": "b"},
            {"question": "What is forward bias in a p-n junction diode?", "options": {"a": "Connecting positive terminal of battery to n-type and negative to p-type", "b": "Connecting positive terminal of battery to p-type and negative to n-type", "c": "Connecting both terminals to the n-type material", "d": "Short-circuiting the diode"}, "correctAnswer": "b"},
            {"question": "What is the primary function of a rectifier diode in an electronic circuit?", "options": {"a": "To amplify voltage signals", "b": "To convert alternating current (AC) to direct current (DC)", "c": "To store electrical energy", "d": "To act as a variable resistor"}, "correctAnswer": "b"},
            {"question": "A bipolar junction transistor (BJT) has three terminals called the:", "options": {"a": "Anode, Cathode, Gate", "b": "Emitter, Base, Collector", "c": "Source, Drain, Gate", "d": "Positive, Negative, Neutral"}, "correctAnswer": "b"},
            {"question": "In a transistor, which region is very thin and lightly doped?", "options": {"a": "Emitter", "b": "Base", "c": "Collector", "d": "PN boundary"}, "correctAnswer": "b"},
            {"question": "The current gain beta (hFE) of a transistor is the ratio of:", "options": {"a": "Base current to collector current", "b": "Collector current to base current (IC / IB)", "c": "Emitter current to collector current", "d": "Collector current to emitter current"}, "correctAnswer": "b"},
            {"question": "A full-wave bridge rectifier circuit requires a minimum of how many diodes?", "options": {"a": "1", "b": "4", "c": "2", "d": "6"}, "correctAnswer": "b"},
            {"question": "What is the minority carrier in a p-type semiconductor?", "options": {"a": "Holes", "b": "Electrons", "c": "Acceptor atoms", "d": "Donor atoms"}, "correctAnswer": "b"},
            {"question": "A depletion region is formed at:", "options": {"a": "A pure copper wire contact", "b": "The boundary of a p-n junction", "c": "The emitter-collector terminal only", "d": "Inside the dielectric of a capacitor"}, "correctAnswer": "b"}
        ]
        
    elif chapter_idx == 10:  # Modern Physics
        pool = [
            {"question": "The photoelectric effect is the emission of electrons from the surface of a metal when:", "options": {"a": "It is heated to a very high temperature", "b": "Light of a suitable frequency falls on it", "c": "An electric voltage is applied across it", "d": "It is placed in a strong magnetic field"}, "correctAnswer": "b"},
            {"question": "According to quantum theory, light is emitted and absorbed in discrete packets of energy called:", "options": {"a": "Electrons", "b": "Photons", "c": "Protons", "d": "Phonons"}, "correctAnswer": "b"},
            {"question": "The energy of a single photon is given by the formula:", "options": {"a": "E = h / f", "b": "E = h * f", "c": "E = h * lambda", "d": "E = f / h"}, "correctAnswer": "b"},
            {"question": "In Einstein's photoelectric equation, what does the term 'work function' (Phi) represent?", "options": {"a": "The kinetic energy of the emitted photoelectrons", "b": "The minimum energy required to liberate an electron from the metal surface", "c": "The potential energy of the atom in the metal lattice", "d": "The total energy of the incident photon"}, "correctAnswer": "b"},
            {"question": "The threshold frequency is defined as the:", "options": {"a": "Maximum frequency of light that will NOT emit electrons", "b": "Minimum frequency of incident light required to cause photoelectric emission", "c": "Frequency of emitted electrons from the metal", "d": "Frequency of light at which total internal reflection occurs"}, "correctAnswer": "b"},
            {"question": "Who proposed the hypothesis that moving particles (like electrons) exhibit wave-like properties?", "options": {"a": "Albert Einstein", "b": "Louis de Broglie", "c": "Max Planck", "d": "Niels Bohr"}, "correctAnswer": "b"},
            {"question": "The de Broglie wavelength (lambda) of a particle of mass m moving with velocity v is given by:", "options": {"a": "lambda = h * m * v", "b": "lambda = h / (m * v)", "c": "lambda = m * v / h", "d": "lambda = h / sqrt(m * v)"}, "correctAnswer": "b"},
            {"question": "What is Planck's constant (h) approximately equal to?", "options": {"a": "3.00 x 10^8 m/s", "b": "6.63 x 10^-34 J*s", "c": "1.60 x 10^-19 C", "d": "9.11 x 10^-31 kg"}, "correctAnswer": "b"},
            {"question": "The wave-particle duality refers to the fact that:", "options": {"a": "Waves and particles are completely unrelated concepts", "b": "Light and matter exhibit both wave-like and particle-like properties depending on the experiment", "c": "Waves can be converted into solid mass in chemical reactions", "d": "Light consists of electrons propagating in wave packets"}, "correctAnswer": "b"},
            {"question": "Einstein's mass-energy equivalence equation is:", "options": {"a": "E = m * c", "b": "E = m * c^2", "c": "E = 1/2 * m * v^2", "d": "E = h * c / lambda"}, "correctAnswer": "b"},
            {"question": "The maximum kinetic energy of photoelectrons emitted from a metal surface depends on:", "options": {"a": "The intensity of the incident light only", "b": "The frequency of the incident light and the work function of the metal", "c": "The area of the metal surface exposed", "d": "The duration of light exposure"}, "correctAnswer": "b"},
            {"question": "If the intensity of light falling on a photoelectric cell is doubled, what happens to the number of emitted photoelectrons?", "options": {"a": "It remains unchanged", "b": "It is doubled", "c": "It is halved", "d": "It increases four times"}, "correctAnswer": "b"},
            {"question": "What is the stopping potential in a photoelectric experiment?", "options": {"a": "The potential difference that accelerates photoelectrons to maximum speed", "b": "The retarding potential difference required to stop the fastest photoelectrons from reaching the anode", "c": "The voltage at which the light source turns off automatically", "d": "The work function expressed in volts"}, "correctAnswer": "b"},
            {"question": "In the dual nature of light, which experiment demonstrates the particle nature of light?", "options": {"a": "Young's double-slit experiment", "b": "Photoelectric effect", "c": "Diffraction of light by a single slit", "d": "Polarization of light"}, "correctAnswer": "b"},
            {"question": "According to the de Broglie relation, as the momentum of a particle increases, its wavelength:", "options": {"a": "Increases", "b": "Decreases", "c": "Remains constant", "d": "Becomes zero"}, "correctAnswer": "b"}
        ]
        
    elif chapter_idx == 11:  # Nuclear Physics
        pool = [
            {"question": "What is an isotope?", "options": {"a": "Atoms of different elements with the same mass number", "b": "Atoms of the same element with the same atomic number but different mass numbers due to neutron differences", "c": "Atoms that do not have any electrons orbiting the nucleus", "d": "Unstable elements that decay only by emitting neutrons"}, "correctAnswer": "b"},
            {"question": "What is the mass number (A) of an atom?", "options": {"a": "The number of protons in the nucleus", "b": "The total number of protons and neutrons in the nucleus", "c": "The number of electrons orbiting the nucleus", "d": "The atomic mass measured in grams"}, "correctAnswer": "b"},
            {"question": "What is the atomic number (Z) of an atom?", "options": {"a": "The total number of protons and neutrons", "b": "The number of protons in the nucleus", "c": "The number of neutrons in the nucleus", "d": "The number of isotopes of the element"}, "correctAnswer": "b"},
            {"question": "What are the three main types of radiation emitted during radioactive decay?", "options": {"a": "Protons, neutrons, and electrons", "b": "Alpha particles, beta particles, and gamma rays", "c": "X-rays, ultraviolet rays, and infrared rays", "d": "Cathode rays, anode rays, and cosmic rays"}, "correctAnswer": "b"},
            {"question": "An alpha particle consists of:", "options": {"a": "A high-speed electron emitted from the nucleus", "b": "A helium nucleus containing 2 protons and 2 neutrons", "c": "A high-energy photon", "d": "A single unstable neutron"}, "correctAnswer": "b"},
            {"question": "A beta-minus particle is:", "options": {"a": "A helium nucleus", "b": "A high-energy electron emitted from the nucleus during decay", "c": "A positive proton", "d": "An uncharged neutron"}, "correctAnswer": "b"},
            {"question": "Gamma radiation consists of:", "options": {"a": "High-speed helium nuclei", "b": "High-energy electromagnetic radiation (photons)", "c": "Negatively charged electrons", "d": "Positively charged protons"}, "correctAnswer": "b"},
            {"question": "What is the half-life of a radioactive substance?", "options": {"a": "Half the time required for the entire sample to decay", "b": "The time required for half of the radioactive nuclei in a sample to decay", "c": "The time it takes for an atom to lose half of its mass", "d": "The age of the oldest radioactive isotope in the sample"}, "correctAnswer": "b"},
            {"question": "Nuclear fission is the process in which:", "options": {"a": "Two light nuclei combine to form a heavier nucleus", "b": "A heavy nucleus splits into two or more smaller nuclei with the release of energy", "c": "An electron is captured by a proton in the nucleus", "d": "Radioactive particles are completely neutralized"}, "correctAnswer": "b"},
            {"question": "Nuclear fusion is the process in which:", "options": {"a": "A heavy nucleus splits into lighter nuclei", "b": "Two light nuclei combine to form a heavier, more stable nucleus with the release of energy", "c": "Electrons are ejected from a metal plate by light", "d": "A neutron decays into a proton and an electron"}, "correctAnswer": "b"},
            {"question": "The difference between the rest mass of a nucleus and the sum of the rest masses of its individual nucleons is called the:", "options": {"a": "Mass defect", "b": "Binding energy", "c": "Fission energy", "d": "Isotope fraction"}, "correctAnswer": "a"},
            {"question": "The energy equivalent to the mass defect that holds the nucleus together is called the:", "options": {"a": "Critical energy", "b": "Binding energy", "c": "Activation energy", "d": "Ionization energy"}, "correctAnswer": "b"},
            {"question": "Which of the following radiations has the highest penetrating power?", "options": {"a": "Alpha particles", "b": "Gamma rays", "c": "Beta particles", "d": "Neutron beams"}, "correctAnswer": "b"},
            {"question": "Which of the following radiations has the highest ionizing power?", "options": {"a": "Gamma rays", "b": "Alpha particles", "c": "Beta particles", "d": "X-rays"}, "correctAnswer": "b"},
            {"question": "What is the binding energy equivalent of 1 atomic mass unit (amu)?", "options": {"a": "9.1 x 10^-31 J", "b": "931.5 MeV", "c": "1.6 x 10^-19 J", "d": "3.0 x 10^8 eV"}, "correctAnswer": "b"}
        ]
        
    return pool

def generate_physics_questions_for_chapter(ch_idx):
    """
    Generates exactly 26 easy, 30 medium, and 35 hard questions in English for the given chapter index (1-indexed).
    Combines conceptual questions with dynamically computed calculation questions.
    """
    questions = []
    conceptual = make_conceptual_pool(ch_idx)
    
    # ------------------ EASY QUESTIONS (26) ------------------
    easy_list = []
    # Fill up to 15 conceptuals first
    for q in conceptual:
        if len(easy_list) < 15:
            easy_list.append({
                "question": q["question"],
                "options": q["options"],
                "correctAnswer": q["correctAnswer"],
                "difficultyLevel": "easy"
            })
            
    # Add simple calculations or basic variations to reach exactly 26
    idx = len(easy_list)
    while len(easy_list) < 26:
        idx += 1
        if ch_idx == 1:  # Oscillatory Motion
            val = idx * 2
            ans = f"{1.0/val:.4f} Hz"
            easy_list.append({
                "question": f"An oscillator completes one full vibration in {val} seconds. What is its frequency?",
                "options": {"a": "2.0 Hz", "b": ans, "c": f"{val} Hz", "d": "0.5 Hz"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
        elif ch_idx == 2:  # Wave Motion
            f_val = idx * 10
            lambda_val = 2
            v_val = f_val * lambda_val
            ans = f"{v_val} m/s"
            easy_list.append({
                "question": f"A wave has a wavelength of {lambda_val} meters and a frequency of {f_val} Hz. Calculate its wave speed.",
                "options": {"a": "5 m/s", "b": ans, "c": f"{f_val/lambda_val} m/s", "d": f"{f_val} m/s"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
        elif ch_idx == 3:  # Sound Waves
            t_val = idx * 0.1
            v_sound = 340
            d_val = round(v_sound * t_val, 1)
            ans = f"{d_val} m"
            easy_list.append({
                "question": f"If sound travels at a speed of 340 m/s in air, what distance does it travel in {t_val:.1f} seconds?",
                "options": {"a": "34 m", "b": ans, "c": f"{d_val * 2} m", "d": "170 m"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
        elif ch_idx == 4:  # Reflection
            f_val = idx * 5
            r_val = f_val * 2
            ans = f"{r_val} cm"
            easy_list.append({
                "question": f"If the focal length of a concave mirror is {f_val} cm, what is the radius of curvature of the mirror?",
                "options": {"a": f"{f_val} cm", "b": ans, "c": f"{f_val/2} cm", "d": f"{f_val*3} cm"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
        elif ch_idx == 5:  # Refraction
            f_val = idx * 0.1
            p_val = round(1.0 / f_val, 2)
            ans = f"{p_val} D"
            easy_list.append({
                "question": f"A converging lens has a focal length of {f_val:.2f} meters. What is the power of the lens in Dioptres?",
                "options": {"a": f"{f_val} D", "b": ans, "c": "1.0 D", "d": f"{p_val*2} D"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
        elif ch_idx == 6:  # Dispersion
            n_val = 1.5 + (idx * 0.02)
            c_val = round(3 * 10**8 / n_val, 2)
            ans = f"{c_val/10**8:.2f} x 10^8 m/s"
            easy_list.append({
                "question": f"If the refractive index of a glass block is {n_val:.2f}, what is the speed of light inside it? (Use speed of light in vacuum c = 3.0 x 10^8 m/s)",
                "options": {"a": "3.0 x 10^8 m/s", "b": ans, "c": "2.0 x 10^8 m/s", "d": "1.5 x 10^8 m/s"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
        elif ch_idx == 7:  # Electromagnetic Induction
            n_val = idx * 50
            dphi = 2
            dt = 0.5
            emf = int(n_val * dphi / dt)
            ans = f"{emf} V"
            easy_list.append({
                "question": f"A coil has {n_val} turns. If the magnetic flux passing through it changes by 2 Wb in 0.5 seconds, what is the magnitude of the induced electromotive force (emf)?",
                "options": {"a": f"{n_val} V", "b": ans, "c": f"{emf/2} V", "d": "100 V"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
        elif ch_idx == 8:  # AC
            v0 = idx * 10
            vrms = round(v0 / math.sqrt(2), 2)
            ans = f"{vrms} V"
            easy_list.append({
                "question": f"If the peak voltage of an AC source is {v0} V, what is the root-mean-square (RMS) voltage?",
                "options": {"a": f"{v0} V", "b": ans, "c": f"{v0*2} V", "d": "12 V"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
        elif ch_idx == 9:  # Electronics
            val = idx * 5
            ans = f"{val} mA"
            easy_list.append({
                "question": f"In a transistor, if the emitter current is {val + 0.5:.1f} mA and the base current is 0.5 mA, what is the collector current?",
                "options": {"a": "0.5 mA", "b": ans, "c": f"{val + 1} mA", "d": "1.0 mA"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
        elif ch_idx == 10:  # Modern Physics
            val = idx * 2
            ans = f"{val/3.0:.3f} x 10^8 m/s"
            easy_list.append({
                "question": f"What is the speed of a particle whose relativistic mass is {val} times its rest mass? Express relative to c.",
                "options": {"a": "3.0 x 10^8 m/s", "b": f"{math.sqrt(1 - 1.0/(val**2))*3.0:.2f} x 10^8 m/s", "c": "1.5 x 10^8 m/s", "d": "Zero"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
        else:  # Nuclear Physics
            neutrons = idx * 2
            protons = idx + 1
            mass_num = neutrons + protons
            easy_list.append({
                "question": f"An isotope of an element contains {protons} protons and {neutrons} neutrons. What is the mass number of this isotope?",
                "options": {"a": f"{protons}", "b": f"{mass_num}", "c": f"{neutrons}", "d": f"{abs(neutrons-protons)}"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
            
    # ------------------ MEDIUM QUESTIONS (30) ------------------
    med_list = []
    # Fill remaining conceptuals first
    for q in conceptual[15:]:
        if len(med_list) < 10:
            med_list.append({
                "question": q["question"],
                "options": q["options"],
                "correctAnswer": q["correctAnswer"],
                "difficultyLevel": "medium"
            })
            
    # Generate moderate calculations to hit exactly 30
    idx = len(med_list)
    while len(med_list) < 30:
        idx += 1
        if ch_idx == 1:
            l_val = idx * 0.5
            t_val = round(2 * math.pi * math.sqrt(l_val / 9.8), 2)
            ans = f"{t_val} s"
            med_list.append({
                "question": f"A simple pendulum has a string of length {l_val:.2f} meters. Calculate the period of its oscillation. (Use g = 9.8 m/s²)",
                "options": {"a": "1.00 s", "b": ans, "c": f"{t_val*2:.2f} s", "d": "0.50 s"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
        elif ch_idx == 2:
            v_val = 300
            f_val = idx * 20
            lambda_val = round(v_val / f_val, 2)
            ans = f"{lambda_val} m"
            med_list.append({
                "question": f"A wave propagating at {v_val} m/s has a frequency of {f_val} Hz. Calculate the wavelength of the wave.",
                "options": {"a": "1.0 m", "b": ans, "c": f"{lambda_val*2:.2f} m", "d": "0.5 m"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
        elif ch_idx == 3:
            f1 = idx * 10
            f2 = f1 + 3
            ans = "3 Hz"
            med_list.append({
                "question": f"Two tuning forks with frequencies of {f1} Hz and {f2} Hz are sounded simultaneously. What is the resulting beat frequency?",
                "options": {"a": f"{f1+f2} Hz", "b": ans, "c": "6 Hz", "d": "1 Hz"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
        elif ch_idx == 4:
            do_val = idx * 4
            f_val = 12
            if do_val == 12:
                do_val = 15
            di_val = round((12 * do_val) / (do_val - 12), 2)
            ans = f"{di_val} cm"
            med_list.append({
                "question": f"An object is placed at a distance of {do_val} cm in front of a concave mirror of focal length {f_val} cm. Where is the image formed?",
                "options": {"a": "12.0 cm", "b": ans, "c": f"{abs(di_val)*1.5:.2f} cm", "d": "6.0 cm"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
        elif ch_idx == 5:
            n_glass = 1.5
            angle_inc = 30
            # sin(r) = sin(30) / 1.5 = 0.5 / 1.5 = 1/3 => r = arcsin(1/3) = 19.47
            ans = "19.5 degrees"
            med_list.append({
                "question": f"A ray of light enters a glass block of refractive index 1.5 from air. If the angle of incidence is {angle_inc} degrees, calculate the angle of refraction.",
                "options": {"a": "30.0 degrees", "b": ans, "c": "45.0 degrees", "d": "15.0 degrees"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
        elif ch_idx == 6:
            n_val = 1.3 + (idx * 0.01)
            c_val = round(math.degrees(math.asin(1.0 / n_val)), 1)
            ans = f"{c_val} degrees"
            med_list.append({
                "question": f"A transparent medium has a refractive index of {n_val:.2f}. Calculate the critical angle for light traveling from this medium into air.",
                "options": {"a": "90.0 degrees", "b": ans, "c": f"{c_val - 5:.1f} degrees", "d": f"{c_val + 5:.1f} degrees"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
        elif ch_idx == 7:
            a_val = idx * 0.1
            b_val = 0.5
            phi_val = round(b_val * a_val, 4)
            ans = f"{phi_val} Wb"
            med_list.append({
                "question": f"A flat loop of wire enclosing an area of {a_val:.2f} m² is oriented perpendicular to a magnetic field of {b_val} T. What is the magnetic flux through the loop?",
                "options": {"a": "1.0 Wb", "b": ans, "c": f"{phi_val * 2} Wb", "d": "0.1 Wb"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
        elif ch_idx == 8:
            r_val = idx * 5
            x_l = 40
            x_c = 10
            z_val = round(math.sqrt(r_val**2 + (x_l - x_c)**2), 2)
            ans = f"{z_val} Ohm"
            med_list.append({
                "question": f"An AC circuit has a resistance of R = {r_val} Ohm, an inductive reactance of X_L = {x_l} Ohm, and a capacitive reactance of X_C = {x_c} Ohm. Calculate the total impedance (Z) of the circuit.",
                "options": {"a": f"{r_val+x_l+x_c} Ohm", "b": ans, "c": f"{z_val*2:.2f} Ohm", "d": "50 Ohm"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
        elif ch_idx == 9:
            base_curr = idx * 10
            beta = 100
            coll_curr = base_curr * beta / 1000.0  # mA
            ans = f"{coll_curr:.2f} mA"
            med_list.append({
                "question": f"A transistor connected in a common-emitter configuration has a current gain (beta) of {beta}. If the base current is {base_curr} microamperes, what is the collector current?",
                "options": {"a": "1.0 mA", "b": ans, "c": f"{coll_curr * 2:.2f} mA", "d": "5.0 mA"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
        elif ch_idx == 10:
            f_val = idx * 10**14
            e_val = 6.63 * 10**-34 * f_val
            ans = f"{e_val:.2e} J"
            med_list.append({
                "question": f"Calculate the energy of a photon of light having a frequency of {f_val:.1e} Hz. (Planck's constant h = 6.63 x 10^-34 J*s)",
                "options": {"a": "1.6 x 10^-19 J", "b": ans, "c": "3.0 x 10^8 J", "d": f"{e_val*2:.1e} J"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
        else:  # Nuclear Physics
            halflife = idx * 2
            ans = "12.5%"
            med_list.append({
                "question": f"A radioactive isotope has a half-life of {halflife} days. What percentage of the original active isotope will remain after {halflife * 3} days?",
                "options": {"a": "50.0%", "b": ans, "c": "25.0%", "d": "6.25%"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
            
    # ------------------ HARD QUESTIONS (35) ------------------
    hard_list = []
    idx = 0
    while len(hard_list) < 35:
        idx += 1
        if ch_idx == 1:
            k_val = idx * 10
            m_val = 0.5
            f_val = round((1.0 / (2 * math.pi)) * math.sqrt(k_val / m_val), 2)
            ans = f"{f_val} Hz"
            hard_list.append({
                "question": f"A mass of {m_val} kg is attached to a spring of spring constant k = {k_val} N/m. The system is set into simple harmonic motion. Determine the frequency of the oscillation.",
                "options": {"a": "1.00 Hz", "b": ans, "c": f"{f_val*2:.2f} Hz", "d": "0.50 Hz"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
        elif ch_idx == 2:
            v_val = 340
            f_val = idx * 50
            l_val = round(v_val / f_val, 4)
            t_val = round(1.0 / f_val, 5)
            ans = f"wavelength = {l_val} m, period = {t_val} s"
            hard_list.append({
                "question": f"A sound wave in air propagates at {v_val} m/s with a frequency of {f_val} Hz. Find both its wavelength and its period.",
                "options": {"a": "wavelength = 1.0 m, period = 0.1 s", "b": ans, "c": f"wavelength = {l_val*2} m, period = {t_val*2} s", "d": "wavelength = 0.5 m, period = 0.01 s"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
        elif ch_idx == 3:
            v_s = 340
            v_src = idx * 2
            f_src = 400
            f_obs = int(f_src * (v_s / (v_s - v_src)))
            ans = f"{f_obs} Hz"
            hard_list.append({
                "question": f"An ambulance sounding a siren of frequency 400 Hz approaches a stationary observer at a constant speed of {v_src} m/s. What is the frequency heard by the observer? (Assume speed of sound in air is 340 m/s)",
                "options": {"a": "400 Hz", "b": ans, "c": f"{f_src - 20} Hz", "d": f"{f_obs + 50} Hz"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
        elif ch_idx == 4:
            f_val = - (idx * 5)
            do_val = idx * 10
            di_val = round((f_val * do_val) / (do_val - f_val), 2)
            ans = f"{di_val} cm"
            hard_list.append({
                "question": f"An object is placed at a distance of {do_val} cm from a convex mirror of focal length {abs(f_val)} cm. What is the position of the image formed?",
                "options": {"a": f"{f_val} cm", "b": ans, "c": f"{abs(di_val)} cm", "d": "10.0 cm"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
        elif ch_idx == 5:
            f1 = idx * 5
            f2 = idx * 10
            F = round((f1 * f2) / (f1 + f2), 2)
            ans = f"{F} cm"
            hard_list.append({
                "question": f"Two thin converging lenses with focal lengths of {f1} cm and {f2} cm are placed in contact. Find the effective focal length of the combined lens system.",
                "options": {"a": f"{f1+f2} cm", "b": ans, "c": f"{f1} cm", "d": f"{F*2:.2f} cm"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
        elif ch_idx == 6:
            A_prism = 60
            D_min = 30 + idx
            rad_val = math.radians((A_prism + D_min) / 2.0)
            rad_half = math.radians(A_prism / 2.0)
            n_val = round(math.sin(rad_val) / math.sin(rad_half), 3)
            ans = f"n = {n_val}"
            hard_list.append({
                "question": f"An equilateral glass prism has a prism angle of 60 degrees. If the angle of minimum deviation for a monochromatic ray is {D_min} degrees, calculate the refractive index of the glass.",
                "options": {"a": "n = 1.333", "b": ans, "c": f"n = {n_val + 0.1:.3f}", "d": "n = 1.667"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
        elif ch_idx == 7:
            n_turns = idx * 100
            b_field = 0.2
            radius = 0.05
            dphi_dt = b_field * math.pi * (radius**2) / 0.1
            emf_ind = round(n_turns * dphi_dt, 2)
            ans = f"{emf_ind} V"
            hard_list.append({
                "question": f"A circular coil of {n_turns} turns and radius {radius} m is placed perpendicular to a magnetic field of 0.2 T. If the magnetic field is reduced to zero in 0.1 seconds, what is the average emf induced in the coil?",
                "options": {"a": "10.0 V", "b": ans, "c": f"{emf_ind * 2:.2f} V", "d": "1.00 V"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
        elif ch_idx == 8:
            l_val = idx * 0.1
            c_val = 10 * 10**-6
            f_res = round(1.0 / (2 * math.pi * math.sqrt(l_val * c_val)), 1)
            ans = f"{f_res} Hz"
            hard_list.append({
                "question": f"A series RLC circuit has an inductor of L = {l_val:.2f} H and a capacitor of C = 10 microfarads. Determine the resonant frequency of this circuit.",
                "options": {"a": "50.0 Hz", "b": ans, "c": f"{f_res*2:.1f} Hz", "d": "100.0 Hz"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
        elif ch_idx == 9:
            r_in = 1000
            r_load = 5000 + (idx * 500)
            beta_val = 100 + idx
            v_gain = round(beta_val * (r_load / r_in), 1)
            ans = f"{v_gain}"
            hard_list.append({
                "question": f"A common-emitter transistor amplifier has an input resistance of {r_in} Ohm, a load resistance of {r_load} Ohm, and a current gain of {beta_val}. Determine the voltage gain of the amplifier.",
                "options": {"a": f"{beta_val}", "b": ans, "c": f"{v_gain*2:.1f}", "d": "50.0"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
        elif ch_idx == 10:
            wf = 2.0
            hf = 2.0 + (idx * 0.1)
            kmax = round(hf - wf, 2)
            ans = f"{kmax} eV"
            hard_list.append({
                "question": f"Monochromatic light with a photon energy of {hf:.2f} eV is incident on a metal surface whose work function is {wf:.2f} eV. Calculate the maximum kinetic energy (K_max) of the ejected photoelectrons.",
                "options": {"a": f"{hf} eV", "b": ans, "c": f"{wf} eV", "d": "0.0 eV"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
        else:  # Nuclear Physics
            mass_defect = idx * 0.005 + 0.02
            e_val = round(mass_defect * 931.5, 2)
            ans = f"{e_val} MeV"
            hard_list.append({
                "question": f"In a nuclear reaction, the mass defect is calculated to be {mass_defect:.4f} atomic mass units (amu). Calculate the total binding energy released in the reaction. (Use 1 amu = 931.5 MeV)",
                "options": {"a": "931.5 MeV", "b": ans, "c": f"{e_val*2:.2f} MeV", "d": "10.0 MeV"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
            
    return easy_list + med_list + hard_list

def main():
    print("Beginning Physics subject generation in English...")
    
    titles = {
        1: "Oscillatory Motion",
        2: "Wave Motion",
        3: "Sound Waves",
        4: "Reflection of Light",
        5: "Refraction of Light",
        6: "Dispersion of Light",
        7: "Electromagnetic Induction",
        8: "Alternating Current",
        9: "Electronics",
        10: "Modern Physics",
        11: "Nuclear Physics"
    }
    
    final_physics_chapters = []
    total_written = 0
    
    for i in range(1, 12):
        ch_id = f"phy_ch{i}"
        ch_questions = generate_physics_questions_for_chapter(i)
        
        # Format IDs sequentially: Phy_Ch{i}_Q{01-91}
        formatted_qs = []
        for idx, q in enumerate(ch_questions):
            q_id = f"Phy_Ch{i}_Q{idx+1:02d}"
            options_clean = {k.lower(): str(v) for k, v in q["options"].items()}
            formatted_qs.append({
                "id": q_id,
                "question": q["question"],
                "options": options_clean,
                "correctAnswer": q["correctAnswer"].lower(),
                "difficultyLevel": q["difficultyLevel"],
                "subjectId": "phy",
                "chapterId": ch_id
            })
            
        ch_easy = [q for q in formatted_qs if q["difficultyLevel"] == "easy"]
        ch_med = [q for q in formatted_qs if q["difficultyLevel"] == "medium"]
        ch_hard = [q for q in formatted_qs if q["difficultyLevel"] == "hard"]
        
        print(f"Chapter {i} ({titles[i]}): Total={len(formatted_qs)} (Easy={len(ch_easy)}, Medium={len(ch_med)}, Hard={len(ch_hard)})")
        
        # Verify counts
        assert len(ch_easy) == 26, f"Ch {i} easy is {len(ch_easy)}, expected 26"
        assert len(ch_med) == 30, f"Ch {i} medium is {len(ch_med)}, expected 30"
        assert len(ch_hard) == 35, f"Ch {i} hard is {len(ch_hard)}, expected 35"
        
        final_physics_chapters.append({
            "id": ch_id,
            "subjectId": "phy",
            "title": titles[i],
            "questions": formatted_qs
        })
        total_written += len(formatted_qs)
        
    print(f"Total Physics questions compiled: {total_written}")
    
    # 2. Modify lib/services/seed_data.dart
    print("Reading seed_data.dart...")
    with open(DART_FILE, "r", encoding="utf-8") as f:
        content = f.read()
        
    start_str = "const String fullSeedJson = r'''"
    start_idx = content.find('{', content.find(start_str))
    end_idx = content.rfind("''';")
    
    if start_idx == -1 or end_idx == -1:
        print("Error: Could not locate JSON boundaries in seed_data.dart")
        return
        
    json_string = content[start_idx:end_idx].strip()
    data = json.loads(json_string)
    
    # Rebuild the subjects list in seed_data.dart
    subjects = data.get("subjects", [])
    
    # Find existing physics subject (id: 'phy')
    physics_idx = -1
    for idx, s in enumerate(subjects):
        if s.get("id") == "phy" or s.get("name") == "Physics":
            physics_idx = idx
            break
            
    new_physics_chapters_format = []
    for ch in final_physics_chapters:
        new_physics_chapters_format.append({
            "title": ch["title"],
            "questions": ch["questions"]
        })
        
    new_physics_subject = {
        "name": "Physics",
        "id": "phy",
        "chapters": new_physics_chapters_format
    }
    
    if physics_idx != -1:
        subjects[physics_idx] = new_physics_subject
        print("Replaced existing Physics subject in subjects list.")
    else:
        subjects.append(new_physics_subject)
        print("Appended new Physics subject in subjects list.")
        
    # Rebuild the final json string
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content[:start_idx] + new_json_str + "\n" + content[end_idx:]
    
    print("Writing updated seed_data.dart...")
    with open(DART_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully updated seed_data.dart!")
    
    # 3. Update seed_data.json if it exists
    if os.path.exists(JSON_FILE):
        print("Reading and updating seed_data.json...")
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            data_json = json.load(f)
            
        # Update subjects dictionary
        if "subjects" not in data_json:
            data_json["subjects"] = {}
        data_json["subjects"]["phy"] = {"name": "Physics"}
        
        # Update chapters dictionary
        if "chapters" not in data_json:
            data_json["chapters"] = {}
        # Clear existing physics chapters first
        keys_to_remove = [k for k, v in data_json["chapters"].items() if v.get("subjectId") == "phy"]
        for k in keys_to_remove:
            del data_json["chapters"][k]
            
        # Add new chapters
        for ch in final_physics_chapters:
            data_json["chapters"][ch["id"]] = {
                "subjectId": "phy",
                "title": ch["title"]
            }
            
        # Update questions dictionary
        if "questions" not in data_json:
            data_json["questions"] = {}
        # Clear existing physics questions
        keys_to_remove = [k for k, v in data_json["questions"].items() if v.get("subjectId") == "phy" or v.get("chapterId", "").startswith("phy_")]
        for k in keys_to_remove:
            del data_json["questions"][k]
            
        # Add all new questions
        for ch in final_physics_chapters:
            for q in ch["questions"]:
                data_json["questions"][q["id"]] = {
                    "question": q["question"],
                    "options": q["options"],
                    "correctAnswer": q["correctAnswer"],
                    "difficultyLevel": q["difficultyLevel"],
                    "subjectId": "phy",
                    "chapterId": q["chapterId"]
                }
            
        # Re-save seed_data.json
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(data_json, f, indent=2, ensure_ascii=False)
        print("Successfully updated seed_data.json!")
    else:
        print("seed_data.json not found, skipping.")

if __name__ == "__main__":
    main()
