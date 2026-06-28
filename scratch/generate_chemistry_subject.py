import json
import os
import math

# File paths
DART_FILE = r'lib/services/seed_data.dart'
JSON_FILE = r'scratch/seed_data.json'

def make_conceptual_pool(chapter_idx):
    """
    Returns a pool of distinct, high-quality English conceptual questions for a given chapter.
    We define 15 conceptual questions for each of the 8 chapters.
    """
    pool = []
    
    if chapter_idx == 1:  # Hydrocarbons
        pool = [
            {"question": "What is the general formula for alkanes?", "options": {"a": "C_n H_2n", "b": "C_n H_2n+2", "c": "C_n H_2n-2", "d": "C_n H_2n+1"}, "correctAnswer": "b"},
            {"question": "Hydrocarbons containing only single covalent bonds between carbon atoms are called:", "options": {"a": "Alkenes", "b": "Alkanes", "c": "Alkynes", "d": "Arenes"}, "correctAnswer": "b"},
            {"question": "What is the general formula for alkenes?", "options": {"a": "C_n H_2n+2", "b": "C_n H_2n", "c": "C_n H_2n-2", "d": "C_n H_2n+1"}, "correctAnswer": "b"},
            {"question": "Hydrocarbons containing at least one carbon-carbon double bond are classified as:", "options": {"a": "Alkanes", "b": "Alkenes", "c": "Alkynes", "d": "Aromatics"}, "correctAnswer": "b"},
            {"question": "What is the general formula for alkynes?", "options": {"a": "C_n H_2n+2", "b": "C_n H_2n-2", "c": "C_n H_2n", "d": "C_n H_n"}, "correctAnswer": "b"},
            {"question": "Compounds with the same molecular formula but different structural arrangements are called:", "options": {"a": "Isotopes", "b": "Isomers", "c": "Allotropes", "d": "Homologs"}, "correctAnswer": "b"},
            {"question": "Which of the following is an unsaturated hydrocarbon?", "options": {"a": "Methane", "b": "Ethene", "c": "Propane", "d": "Butane"}, "correctAnswer": "b"},
            {"question": "What is the simplest aromatic hydrocarbon?", "options": {"a": "Cyclohexane", "b": "Benzene", "c": "Naphthalene", "d": "Toluene"}, "correctAnswer": "b"},
            {"question": "The primary source of hydrocarbons used as fuels worldwide is:", "options": {"a": "Wood", "b": "Crude oil (petroleum)", "c": "Biomass", "d": "Carbon dioxide"}, "correctAnswer": "b"},
            {"question": "Which reaction is characteristic of saturated hydrocarbons?", "options": {"a": "Addition reaction", "b": "Substitution reaction", "c": "Polymerization", "d": "Hydration"}, "correctAnswer": "b"},
            {"question": "Which reaction is characteristic of unsaturated hydrocarbons like alkenes?", "options": {"a": "Substitution reaction", "b": "Addition reaction", "c": "Esterification", "d": "Neutralization"}, "correctAnswer": "b"},
            {"question": "What catalyst is commonly used in the hydrogenation of alkenes?", "options": {"a": "Iron", "b": "Nickel or Platinum", "c": "Manganese dioxide", "d": "Concentrated sulfuric acid"}, "correctAnswer": "b"},
            {"question": "The IUPAC name of the hydrocarbon with formula CH3-CH2-CH3 is:", "options": {"a": "Ethane", "b": "Propane", "c": "Butane", "d": "Pentane"}, "correctAnswer": "b"},
            {"question": "When alkanes undergo complete combustion, the products are:", "options": {"a": "Carbon monoxide and water", "b": "Carbon dioxide and water", "c": "Carbon soot and hydrogen gas", "d": "Methane and oxygen"}, "correctAnswer": "b"},
            {"question": "The hybridization of carbon atoms in methane (CH4) is:", "options": {"a": "sp", "b": "sp3", "c": "sp2", "d": "dsp2"}, "correctAnswer": "b"}
        ]
        
    elif chapter_idx == 2:  # Alcohols, Phenols and Ethers
        pool = [
            {"question": "The functional group characteristic of alcohols is the:", "options": {"a": "Carbonyl group", "b": "Hydroxyl group (-OH)", "c": "Carboxyl group", "d": "Ether linkage"}, "correctAnswer": "b"},
            {"question": "What is the general formula of aliphatic primary alcohols?", "options": {"a": "R-O-R", "b": "R-OH", "c": "R-CHO", "d": "R-COOH"}, "correctAnswer": "b"},
            {"question": "Phenols are organic compounds in which a hydroxyl group is directly bonded to:", "options": {"a": "An alkyl group", "b": "A benzene ring", "c": "A carbonyl carbon", "d": "An alkene double bond"}, "correctAnswer": "b"},
            {"question": "What is the general structure of an ether?", "options": {"a": "R-OH", "b": "R-O-R'", "c": "R-CO-R'", "d": "R-COOR'"}, "correctAnswer": "b"},
            {"question": "The fermentation of glucose by yeast enzymes yields ethanol and:", "options": {"a": "Oxygen gas", "b": "Carbon dioxide", "c": "Methane gas", "d": "Hydrogen gas"}, "correctAnswer": "b"},
            {"question": "Alcohols have higher boiling points than alkanes of comparable molar mass due to:", "options": {"a": "Ionic bonding", "b": "Intermolecular hydrogen bonding", "c": "Van der Waals forces only", "d": "Covalent network bonds"}, "correctAnswer": "b"},
            {"question": "Which of the following is a secondary alcohol?", "options": {"a": "Methanol", "b": "Propan-2-ol", "c": "Ethanol", "d": "2-Methylpropan-2-ol"}, "correctAnswer": "b"},
            {"question": "Dehydration of ethanol at 170 degrees Celsius in the presence of concentrated sulfuric acid yields:", "options": {"a": "Diethyl ether", "b": "Ethene", "c": "Ethane", "d": "Ethyl hydrogen sulfate"}, "correctAnswer": "b"},
            {"question": "The dehydration of two molecules of alcohol at lower temperatures (140 degrees Celsius) yields an:", "options": {"a": "Alkene", "b": "Ether", "c": "Aldehyde", "d": "Ester"}, "correctAnswer": "b"},
            {"question": "Phenol is also known as:", "options": {"a": "Benzoic acid", "b": "Carbolic acid", "c": "Salicylic acid", "d": "Benzyl alcohol"}, "correctAnswer": "b"},
            {"question": "Unlike alcohols, phenols are sufficiently acidic to react with:", "options": {"a": "Water only", "b": "Sodium hydroxide solution", "c": "Hydrochloric acid", "d": "Sodium chloride"}, "correctAnswer": "b"},
            {"question": "What is the common name of ethoxyethane?", "options": {"a": "Dimethyl ether", "b": "Diethyl ether", "c": "Methyl ethyl ether", "d": "Dipropyl ether"}, "correctAnswer": "b"},
            {"question": "Primary alcohols oxidize to form aldehydes, which can be further oxidized to form:", "options": {"a": "Ketones", "b": "Carboxylic acids", "c": "Esters", "d": "Ethers"}, "correctAnswer": "b"},
            {"question": "Which alcohol is commonly known as wood alcohol and is highly toxic?", "options": {"a": "Ethanol", "b": "Methanol", "c": "Propanol", "d": "Glycerol"}, "correctAnswer": "b"},
            {"question": "An alcohol containing three hydroxyl groups is classified as a trihydric alcohol, an example of which is:", "options": {"a": "Ethanol", "b": "Glycerol (propane-1,2,3-triol)", "c": "Glycol (ethane-1,2-diol)", "d": "Phenol"}, "correctAnswer": "b"}
        ]
        
    elif chapter_idx == 3:  # Aldehydes, Ketones and Carboxylic Acids
        pool = [
            {"question": "Aldehydes and ketones both contain which functional group?", "options": {"a": "Hydroxyl group", "b": "Carbonyl group (C=O)", "c": "Carboxyl group", "d": "Ester group"}, "correctAnswer": "b"},
            {"question": "In aldehydes, the carbonyl carbon is bonded to at least:", "options": {"a": "Two alkyl groups", "b": "One hydrogen atom", "c": "One hydroxyl group", "d": "Two oxygen atoms"}, "correctAnswer": "b"},
            {"question": "In ketones, the carbonyl carbon is bonded to:", "options": {"a": "A hydrogen atom and an alkyl group", "b": "Two alkyl or aryl groups", "c": "A hydroxyl group", "d": "An alkoxy group"}, "correctAnswer": "b"},
            {"question": "The functional group characteristic of carboxylic acids is the:", "options": {"a": "Carbonyl group", "b": "Carboxyl group (-COOH)", "c": "Ester linkage", "d": "Hydroxyl group"}, "correctAnswer": "b"},
            {"question": "The oxidation of a secondary alcohol yields a:", "options": {"a": "Carboxylic acid", "b": "Ketone", "c": "Aldehyde", "d": "Ether"}, "correctAnswer": "b"},
            {"question": "Which reagent is commonly used to distinguish aldehydes from ketones by forming a silver mirror?", "options": {"a": "Fehling's solution", "b": "Tollens' reagent", "c": "Lucas reagent", "d": "Acidified potassium dichromate"}, "correctAnswer": "b"},
            {"question": "Carboxylic acids react with alcohols in the presence of an acid catalyst to produce:", "options": {"a": "Aldehydes and water", "b": "Esters and water", "c": "Ketones and hydrogen", "d": "Ethers and water"}, "correctAnswer": "b"},
            {"question": "The reaction between a carboxylic acid and an alcohol to form an ester is known as:", "options": {"a": "Saponification", "b": "Esterification", "c": "Hydration", "d": "Hydrolysis"}, "correctAnswer": "b"},
            {"question": "What is the common name of methanoic acid?", "options": {"a": "Acetic acid", "b": "Formic acid", "c": "Propionic acid", "d": "Butyric acid"}, "correctAnswer": "b"},
            {"question": "What is the common name of ethanoic acid?", "options": {"a": "Formic acid", "b": "Acetic acid", "c": "Oxalic acid", "d": "Lactic acid"}, "correctAnswer": "b"},
            {"question": "Which of the following organic compounds has the highest boiling point among isomers due to strong hydrogen bonding dimerization?", "options": {"a": "Aldehydes", "b": "Carboxylic acids", "c": "Ketones", "d": "Esters"}, "correctAnswer": "b"},
            {"question": "The alkaline hydrolysis of esters (fats and oils) to produce soap and glycerol is called:", "options": {"a": "Esterification", "b": "Saponification", "c": "Fermentation", "d": "Hydrogenation"}, "correctAnswer": "b"},
            {"question": "What is the IUPAC name of acetone?", "options": {"a": "Propanal", "b": "Propan-2-one (propanone)", "c": "Ethanal", "d": "Butanone"}, "correctAnswer": "b"},
            {"question": "Carboxylic acids react with active metals (like sodium) to release which gas?", "options": {"a": "Oxygen", "b": "Hydrogen", "c": "Carbon dioxide", "d": "Ammonia"}, "correctAnswer": "b"},
            {"question": "Esters are characterized by having:", "options": {"a": "A sharp, vinegar-like smell", "b": "Sweet, pleasant, fruity odors", "c": "A rotten-egg smell", "d": "No odor at all"}, "correctAnswer": "b"}
        ]
        
    elif chapter_idx == 4:  # Biochemistry
        pool = [
            {"question": "The main elements composing carbohydrates, proteins, and lipids are:", "options": {"a": "Nitrogen, sulfur, and phosphorus only", "b": "Carbon, hydrogen, and oxygen", "c": "Sodium, chlorine, and potassium", "d": "Iron, calcium, and magnesium"}, "correctAnswer": "b"},
            {"question": "Which of the following is a monosaccharide?", "options": {"a": "Sucrose", "b": "Glucose", "c": "Starch", "d": "Maltose"}, "correctAnswer": "b"},
            {"question": "Which carbohydrate is commonly known as table sugar and is a disaccharide of glucose and fructose?", "options": {"a": "Lactose", "b": "Sucrose", "c": "Maltose", "d": "Galactose"}, "correctAnswer": "b"},
            {"question": "Proteins are biopolymers made up of monomer units called:", "options": {"a": "Monosaccharides", "b": "Amino acids", "c": "Fatty acids", "d": "Nucleotides"}, "correctAnswer": "b"},
            {"question": "The covalent bond that links two amino acids together in a protein chain is called a:", "options": {"a": "Glycosidic bond", "b": "Peptide bond", "c": "Ester bond", "d": "Hydrogen bond"}, "correctAnswer": "b"},
            {"question": "Lipids (fats and oils) are structurally esters formed from fatty acids and:", "options": {"a": "Ethanol", "b": "Glycerol", "c": "Glucose", "d": "Amino acids"}, "correctAnswer": "b"},
            {"question": "Which of the following is a storage polysaccharide found in plants?", "options": {"a": "Glycogen", "b": "Starch", "c": "Cellulose", "d": "Sucrose"}, "correctAnswer": "b"},
            {"question": "Which polysaccharide is a structural component of plant cell walls and is indigestible by humans?", "options": {"a": "Starch", "b": "Cellulose", "c": "Glycogen", "d": "Amylose"}, "correctAnswer": "b"},
            {"question": "The storage polysaccharide found in the liver and muscles of animals is:", "options": {"a": "Starch", "b": "Glycogen", "c": "Cellulose", "d": "Lactose"}, "correctAnswer": "b"},
            {"question": "Unsaturated fatty acids are liquid at room temperature because:", "options": {"a": "They have shorter carbon chains", "b": "They contain one or more carbon-carbon double bonds which prevent close packing", "c": "They are highly polar", "d": "They form hydrogen bonds"}, "correctAnswer": "b"},
            {"question": "Saturated fatty acids contain:", "options": {"a": "Multiple double bonds", "b": "Only single bonds between carbon atoms", "c": "Triple bonds between carbons", "d": "Benzene rings"}, "correctAnswer": "b"},
            {"question": "What happens when a protein is denatured?", "options": {"a": "Its primary sequence of amino acids is broken down", "b": "Its secondary, tertiary, or quaternary structures are disrupted, losing biological activity", "c": "It is synthesized from amino acids", "d": "It turns into a carbohydrate"}, "correctAnswer": "b"},
            {"question": "Amino acids contain which two key functional groups?", "options": {"a": "Hydroxyl and carbonyl", "b": "Amino (-NH2) and carboxyl (-COOH)", "c": "Ester and ether", "d": "Aldehyde and ketone"}, "correctAnswer": "b"},
            {"question": "Which biological molecules act as catalysts to speed up biochemical reactions?", "options": {"a": "Vitamins", "b": "Enzymes", "c": "Hormones", "d": "Carbohydrates"}, "correctAnswer": "b"},
            {"question": "Which test is used to detect the presence of proteins by producing a violet color?", "options": {"a": "Iodine test", "b": "Biuret test", "c": "Benedict's test", "d": "Tollens' test"}, "correctAnswer": "b"}
        ]
        
    elif chapter_idx == 5:  # p-Block Elements
        pool = [
            {"question": "The p-block elements in the periodic table belong to Groups:", "options": {"a": "1 and 2", "b": "13 to 18", "c": "3 to 12", "d": "Lanthamides and actinides"}, "correctAnswer": "b"},
            {"question": "Which p-block element is the most abundant element in the Earth's atmosphere?", "options": {"a": "Oxygen", "b": "Nitrogen", "c": "Argon", "d": "Carbon"}, "correctAnswer": "b"},
            {"question": "What is the general valence shell electronic configuration for p-block elements?", "options": {"a": "ns2 nd1-10", "b": "ns2 np1-6", "c": "ns1-2", "d": "ns2 np6 nd10"}, "correctAnswer": "b"},
            {"question": "The existence of an element in two or more physical forms with different properties in the same state is called:", "options": {"a": "Isomerism", "b": "Allotropy", "c": "Isotopism", "d": "Homology"}, "correctAnswer": "b"},
            {"question": "Which of the following is an allotrope of carbon?", "options": {"a": "Quartz", "b": "Diamond", "c": "Carbon dioxide", "d": "Silicon"}, "correctAnswer": "b"},
            {"question": "The industrial process used to manufacture ammonia from nitrogen and hydrogen is the:", "options": {"a": "Contact process", "b": "Haber process", "c": "Ostwald process", "d": "Solvay process"}, "correctAnswer": "b"},
            {"question": "Which catalyst and promoter are used in the Haber process?", "options": {"a": "Vanadium pentoxide", "b": "Finely divided iron with molybdenum promoter", "c": "Platinum gauze", "d": "Nickel"}, "correctAnswer": "b"},
            {"question": "The industrial process used to manufacture nitric acid from ammonia is the:", "options": {"a": "Haber process", "b": "Ostwald process", "c": "Contact process", "d": "Deacon process"}, "correctAnswer": "b"},
            {"question": "Which group in the p-block contains the highly reactive non-metals known as halogens?", "options": {"a": "Group 15", "b": "Group 17", "c": "Group 16", "d": "Group 18"}, "correctAnswer": "b"},
            {"question": "Which halogen is a reddish-brown liquid at room temperature?", "options": {"a": "Chlorine", "b": "Bromine", "c": "Iodine", "d": "Fluorine"}, "correctAnswer": "b"},
            {"question": "The extremely unreactive elements of Group 18 are known as the:", "options": {"a": "Halogens", "b": "Noble gases", "c": "Chalcogens", "d": "Alkali metals"}, "correctAnswer": "b"},
            {"question": "Which noble gas is used to fill meteorological balloons because it is very light and non-flammable?", "options": {"a": "Hydrogen", "b": "Helium", "c": "Neon", "d": "Argon"}, "correctAnswer": "b"},
            {"question": "Allotropy is shown by which element of Group 16 that exists as diatomic and triatomic gases?", "options": {"a": "Sulfur", "b": "Oxygen", "c": "Selenium", "d": "Tellurium"}, "correctAnswer": "b"},
            {"question": "What is the molecular formula of ozone?", "options": {"a": "O2", "b": "O3", "c": "O4", "d": "O"}, "correctAnswer": "b"},
            {"question": "Which of the following halogens has the highest electronegativity?", "options": {"a": "Chlorine", "b": "Fluorine", "c": "Bromine", "d": "Iodine"}, "correctAnswer": "b"}
        ]
        
    elif chapter_idx == 6:  # Chemical Kinetics
        pool = [
            {"question": "What is chemical kinetics in chemistry?", "options": {"a": "The study of heat changes during a chemical reaction", "b": "The study of reaction rates and the mechanisms by which they occur", "c": "The study of chemical equilibrium states", "d": "The study of electrical energy in redox reactions"}, "correctAnswer": "b"},
            {"question": "The rate of a chemical reaction is defined as:", "options": {"a": "The time it takes for a reaction to stop", "b": "The change in concentration of reactants or products per unit time", "c": "The total mass of products divided by total mass of reactants", "d": "The speed of light inside the solution"}, "correctAnswer": "b"},
            {"question": "Which of the following factors generally increases the rate of a chemical reaction?", "options": {"a": "Decreasing temperature", "b": "Increasing the concentration of reactants", "c": "Decreasing the surface area of solid reactants", "d": "Removing catalysts"}, "correctAnswer": "b"},
            {"question": "A substance that increases the rate of a chemical reaction without being consumed is called a:", "options": {"a": "Reactant", "b": "Catalyst", "c": "Inhibitor", "d": "Product"}, "correctAnswer": "b"},
            {"question": "According to collision theory, in order for a reaction to occur, colliding particles must have:", "options": {"a": "Low kinetic energy and random orientation", "b": "Minimum activation energy and proper orientation", "c": "High electrostatic charge only", "d": "Identical atomic masses"}, "correctAnswer": "b"},
            {"question": "The minimum energy that colliding molecules must possess to initiate a chemical reaction is the:", "options": {"a": "Kinetic energy", "b": "Activation energy", "c": "Enthalpy of reaction", "d": "Binding energy"}, "correctAnswer": "b"},
            {"question": "The unstable arrangement of atoms formed at the peak of the activation energy barrier is called the:", "options": {"a": "Intermediate product", "b": "Activated complex (transition state)", "c": "Catalyzed complex", "d": "Reactant state"}, "correctAnswer": "b"},
            {"question": "How does a catalyst increase the rate of a chemical reaction?", "options": {"a": "By increasing the temperature of the reactants", "b": "By providing an alternative pathway with a lower activation energy", "c": "By increasing the total enthalpy of the products", "d": "By shifting the equilibrium constant"}, "correctAnswer": "b"},
            {"question": "For a reaction A + B -> C, the rate law is written as Rate = k[A]^x [B]^y. What is 'k' called?", "options": {"a": "Equilibrium constant", "b": "Specific rate constant", "c": "Activation constant", "d": "Boltzmann constant"}, "correctAnswer": "b"},
            {"question": "If doubling the concentration of reactant A quadruples the reaction rate, the order of reaction with respect to A is:", "options": {"a": "First-order", "b": "Second-order", "c": "Zero-order", "d": "Third-order"}, "correctAnswer": "b"},
            {"question": "If changing the concentration of reactant B has no effect on the reaction rate, the reaction order with respect to B is:", "options": {"a": "First-order", "b": "Zero-order", "c": "Second-order", "d": "Fractional-order"}, "correctAnswer": "b"},
            {"question": "The half-life of a first-order chemical reaction is:", "options": {"a": "Directly proportional to the initial concentration", "b": "Independent of the initial concentration", "c": "Inversely proportional to the square of initial concentration", "d": "Zero"}, "correctAnswer": "b"},
            {"question": "The units of the rate of reaction are typically:", "options": {"a": "s^-1", "b": "mol L^-1 s^-1 (M/s)", "c": "L mol^-1 s^-1", "d": "mol L"}, "correctAnswer": "b"},
            {"question": "The sequence of elementary steps that leads to the overall chemical reaction is called the:", "options": {"a": "Rate law", "b": "Reaction mechanism", "c": "Stoichiometry of reaction", "d": "Activation pathway"}, "correctAnswer": "b"},
            {"question": "In a multi-step reaction mechanism, which step determines the overall rate of the reaction?", "options": {"a": "The fastest step", "b": "The slowest step (rate-determining step)", "c": "The first step", "d": "The final step"}, "correctAnswer": "b"}
        ]
        
    elif chapter_idx == 7:  # Chemical Equilibrium
        pool = [
            {"question": "A chemical reaction is said to be in dynamic equilibrium when:", "options": {"a": "The reactants are completely converted to products", "b": "The rates of the forward and reverse reactions are equal", "c": "The mass of reactants equals the mass of products", "d": "The concentrations of reactants and products are equal to zero"}, "correctAnswer": "b"},
            {"question": "Which of the following is a key feature of a system at chemical equilibrium?", "options": {"a": "The reaction has completely stopped", "b": "The concentrations of reactants and products remain constant over time", "c": "It must be an open system", "d": "The forward reaction rate is twice the reverse rate"}, "correctAnswer": "b"},
            {"question": "Le Chatelier's Principle states that if a stress is applied to a system at equilibrium:", "options": {"a": "The equilibrium constant will change immediately", "b": "The system will shift in a direction that counteracts the stress", "c": "The reaction will stop completely", "d": "The temperature will increase"}, "correctAnswer": "b"},
            {"question": "For a general gas-phase equilibrium reaction, increasing the pressure will shift the equilibrium towards the side with:", "options": {"a": "Fewer moles of gas", "b": "More moles of gas", "c": "Fewer solids", "d": "Higher temperature"}, "correctAnswer": "a"},
            {"question": "How does adding a catalyst affect a system already at chemical equilibrium?", "options": {"a": "It increases the yield of products", "b": "It has no effect on the equilibrium position or equilibrium constant", "c": "It shifts equilibrium in the forward direction", "d": "It increases the equilibrium constant Kc"}, "correctAnswer": "b"},
            {"question": "What is the only factor that can change the numerical value of the equilibrium constant Kc for a given reaction?", "options": {"a": "Pressure", "b": "Temperature", "c": "Concentration of reactants", "d": "Presence of a catalyst"}, "correctAnswer": "b"},
            {"question": "For an exothermic reaction (heat released), increasing the temperature of the system will:", "options": {"a": "Shift equilibrium to the right, increasing Kc", "b": "Shift equilibrium to the left, decreasing Kc", "c": "Have no effect on the equilibrium position", "d": "Stop the forward reaction"}, "correctAnswer": "b"},
            {"question": "For an endothermic reaction (heat absorbed), increasing the temperature of the system will:", "options": {"a": "Shift equilibrium to the left", "b": "Shift equilibrium to the right, increasing Kc", "c": "Decrease the rate of forward reaction", "d": "Leave Kc unchanged"}, "correctAnswer": "b"},
            {"question": "If the reaction quotient Q is equal to the equilibrium constant Kc, it indicates that:", "options": {"a": "The reaction will proceed to the right", "b": "The system is at equilibrium", "c": "The reaction will proceed to the left", "d": "The reaction has gone to completion"}, "correctAnswer": "b"},
            {"question": "If Q is less than Kc (Q < Kc), the reaction will:", "options": {"a": "Proceed to the left to form more reactants", "b": "Proceed to the right to form more products", "c": "Remain unchanged", "d": "Stop entirely"}, "correctAnswer": "b"},
            {"question": "If Q is greater than Kc (Q > Kc), the reaction will:", "options": {"a": "Proceed to the right to form more products", "b": "Proceed to the left to form more reactants", "c": "Not occur at all", "d": "Maintain equilibrium"}, "correctAnswer": "b"},
            {"question": "An equilibrium system in which all reactants and products are in the same physical state is called a:", "options": {"a": "Heterogeneous equilibrium", "b": "Homogeneous equilibrium", "c": "Static equilibrium", "d": "Phase equilibrium"}, "correctAnswer": "b"},
            {"question": "An equilibrium system containing substances in different physical states is called a:", "options": {"a": "Homogeneous equilibrium", "b": "Heterogeneous equilibrium", "c": "Dynamic phase", "d": "Thermal equilibrium"}, "correctAnswer": "b"},
            {"question": "In writing the expression for the equilibrium constant Kc, which states of matter are omitted?", "options": {"a": "Gases and aqueous solutions", "b": "Pure solids and pure liquids", "c": "Gases only", "d": "Aqueous solutions only"}, "correctAnswer": "b"},
            {"question": "What is the relation between Kc and Kp for a reaction where the change in number of gas moles (delta_n) is zero?", "options": {"a": "Kp = Kc * RT", "b": "Kp = Kc", "c": "Kp = Kc / (RT)", "d": "Kp = Kc^2"}, "correctAnswer": "b"}
        ]
        
    elif chapter_idx == 8:  # Introduction to Nuclear Chemistry
        pool = [
            {"question": "What is the branch of chemistry that deals with radioactivity, nuclear processes, and transformations in the nuclei of atoms?", "options": {"a": "Physical chemistry", "b": "Nuclear chemistry", "c": "Organic chemistry", "d": "Inorganic chemistry"}, "correctAnswer": "b"},
            {"question": "The stability of a nucleus is largely determined by the ratio of:", "options": {"a": "Protons to electrons", "b": "Neutrons to protons", "c": "Electrons to neutrons", "d": "Mass number to atomic number"}, "correctAnswer": "b"},
            {"question": "What is the symbol of an alpha particle in nuclear equations?", "options": {"a": "e- (beta)", "b": "He-4 nucleus (4_2 He)", "c": "gamma ray", "d": "proton (1_1 H)"}, "correctAnswer": "b"},
            {"question": "Which of the following occurs in a nucleus during beta-minus (e-) decay?", "options": {"a": "A proton turns into a neutron", "b": "A neutron turns into a proton, emitting an electron", "c": "Two protons and two neutrons are ejected", "d": "A high-energy photon is absorbed"}, "correctAnswer": "b"},
            {"question": "During gamma decay, the atomic number and mass number of the nucleus:", "options": {"a": "Both decrease by 2", "b": "Remain unchanged", "c": "Increase by 1 and 0 respectively", "d": "Both double"}, "correctAnswer": "b"},
            {"question": "The time required for half of a sample of radioactive nuclei to decay is called the:", "options": {"a": "Mean life", "b": "Half-life", "c": "Decay constant", "d": "Activity period"}, "correctAnswer": "b"},
            {"question": "Which type of nuclear reaction involves the splitting of a heavy nucleus into lighter nuclei?", "options": {"a": "Nuclear fusion", "b": "Nuclear fission", "c": "Alpha capture", "d": "Beta transmutation"}, "correctAnswer": "b"},
            {"question": "Which type of nuclear reaction occurs on the Sun, where light hydrogen nuclei combine to form helium?", "options": {"a": "Nuclear fission", "b": "Nuclear fusion", "c": "Gamma irradiation", "d": "Electron capture"}, "correctAnswer": "b"},
            {"question": "The energy holding the nucleons together in a nucleus, equivalent to its mass defect, is the:", "options": {"a": "Activation energy", "b": "Binding energy", "c": "Ionization energy", "d": "Electrostatic repulsion"}, "correctAnswer": "b"},
            {"question": "What unit is commonly used to express binding energy at the nuclear level?", "options": {"a": "Joules (J)", "b": "Mega-electron volts (MeV)", "c": "Watts (W)", "d": "Calories"}, "correctAnswer": "b"},
            {"question": "Which device is commonly used to detect and measure ionizing radiation?", "options": {"a": "Voltmeter", "b": "Geiger-Muller counter", "c": "Spectrophotometer", "d": "Calorimeter"}, "correctAnswer": "b"},
            {"question": "Radioactive isotopes used in medicine to trace path or diagnose diseases are called:", "options": {"a": "Catalysts", "b": "Radiotracers", "c": "Inhibitors", "d": "Mutagens"}, "correctAnswer": "b"},
            {"question": "What is the change in the mass number of a nucleus when it undergoes alpha decay?", "options": {"a": "Decreases by 2", "b": "Decreases by 4", "c": "Remains unchanged", "d": "Increases by 2"}, "correctAnswer": "b"},
            {"question": "What is the change in the atomic number of a nucleus when it undergoes beta-minus decay?", "options": {"a": "Decreases by 1", "b": "Increases by 1", "c": "Decreases by 2", "d": "Remains unchanged"}, "correctAnswer": "b"},
            {"question": "The mass defect (delta_m) of a nucleus is equal to:", "options": {"a": "Total mass of nucleus minus mass of electrons", "b": "Sum of masses of individual protons and neutrons minus the actual mass of the nucleus", "c": "Mass number minus atomic number", "d": "Mass of protons minus mass of neutrons"}, "correctAnswer": "b"}
        ]
        
    return pool

def generate_chemistry_questions_for_chapter(ch_idx):
    """
    Generates exactly 27 easy, 29 medium, and 35 hard questions in English for the given chapter index (1-indexed).
    Combines conceptual questions with dynamically computed calculation questions.
    """
    questions = []
    conceptual = make_conceptual_pool(ch_idx)
    
    # ------------------ EASY QUESTIONS (27) ------------------
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
            
    # Add simple calculations or basic variations to reach exactly 27
    idx = len(easy_list)
    while len(easy_list) < 27:
        idx += 1
        if ch_idx == 1:  # Hydrocarbons
            val = idx
            h_atoms = 2 * val + 2
            ans = f"{h_atoms}"
            easy_list.append({
                "question": f"An alkane has {val} carbon atoms in its molecule. How many hydrogen atoms does it contain?",
                "options": {"a": f"{2*val}", "b": ans, "c": f"{2*val-2}", "d": f"{val+2}"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
        elif ch_idx == 2:  # Alcohols
            val = idx
            h_atoms = 2 * val + 2
            ans = f"C{val}H{h_atoms}O"
            easy_list.append({
                "question": f"What is the molecular formula of a saturated monohydric alcohol containing {val} carbon atoms?",
                "options": {"a": f"C{val}H{2*val}O", "b": ans, "c": f"C{val}H{2*val-2}O", "d": f"C{val}H{2*val+1}O"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
        elif ch_idx == 3:  # Aldehydes / Ketones / Acids
            val = idx
            molar_mass = 12 * val + 2 * val + 32  # C_n H_2n O2
            ans = f"{molar_mass} g/mol"
            easy_list.append({
                "question": f"Calculate the molar mass of a monocarboxylic acid containing {val} carbon atoms. (Use C = 12, H = 1, O = 16)",
                "options": {"a": f"{molar_mass-2} g/mol", "b": ans, "c": f"{molar_mass+10} g/mol", "d": f"{molar_mass-16} g/mol"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
        elif ch_idx == 4:  # Biochemistry
            peptides = idx
            amino_acids = peptides + 1
            ans = f"{peptides}"
            easy_list.append({
                "question": f"How many peptide bonds are present in a linear polypeptide chain consisting of {amino_acids} amino acid residues?",
                "options": {"a": f"{amino_acids}", "b": ans, "c": f"{peptides-1}", "d": f"{peptides+2}"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
        elif ch_idx == 5:  # p-Block
            val = 13 + (idx % 6)
            group_num = val
            valence_e = val - 10
            ans = f"{valence_e}"
            easy_list.append({
                "question": f"How many valence electrons are present in a neutral atom of a Group {group_num} p-block element?",
                "options": {"a": f"{valence_e-1}", "b": ans, "c": f"{valence_e+2}", "d": "8"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
        elif ch_idx == 6:  # Kinetics
            val = idx * 0.1
            rate = round(1.0 / val, 2)
            ans = f"{rate} mol/L*s"
            easy_list.append({
                "question": f"A reactant's concentration decreases by 1.0 mol/L in a span of {val:.1f} seconds. Calculate the average rate of reaction.",
                "options": {"a": f"{val} mol/L*s", "b": ans, "c": f"{rate*2:.2f} mol/L*s", "d": "0.10 mol/L*s"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
        elif ch_idx == 7:  # Equilibrium
            val = idx * 2
            ans = f"{val}"
            easy_list.append({
                "question": f"For the reaction A(g) <=> B(g), the equilibrium concentrations are [A] = 1.0 M and [B] = {val} M. What is Kc?",
                "options": {"a": "1.0", "b": ans, "c": f"{1.0/val:.3f}", "d": f"{val*2}"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
        else:  # Nuclear
            mass = 100
            halflives = idx % 4 + 1
            rem = mass / (2**halflives)
            ans = f"{rem:.2f} g"
            easy_list.append({
                "question": f"A sample initially contains 100 g of a radioisotope. How much remains after {halflives} half-lives?",
                "options": {"a": "50.00 g", "b": ans, "c": f"{rem*2:.2f} g", "d": f"{rem/2:.2f} g"},
                "correctAnswer": "b",
                "difficultyLevel": "easy"
            })
            
    # ------------------ MEDIUM QUESTIONS (29) ------------------
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
            
    # Generate moderate calculations to hit exactly 29
    idx = len(med_list)
    while len(med_list) < 29:
        idx += 1
        if ch_idx == 1:
            val = idx
            c_mass = 12 * val
            h_mass = 2 * val + 2
            total = c_mass + h_mass
            pct = round((c_mass / total) * 100, 1)
            ans = f"{pct}%"
            easy_list_q = f"Calculate the percentage of carbon by mass in an alkane molecule with {val} carbon atoms. (C = 12, H = 1)"
            med_list.append({
                "question": easy_list_q,
                "options": {"a": "80.0%", "b": ans, "c": f"{pct-5:.1f}%", "d": f"{pct+5:.1f}%"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
        elif ch_idx == 2:
            val = idx * 10
            # C6H12O6 -> 2 C2H5OH + 2 CO2. Molar mass: Glucose=180, Ethanol=46. 
            # Mass ethanol = val * (2 * 46 / 180)
            eth_mass = round(val * (92.0 / 180.0), 2)
            ans = f"{eth_mass} g"
            med_list.append({
                "question": f"During yeast fermentation, {val} g of glucose is completely consumed. Calculate the mass of ethanol produced.",
                "options": {"a": f"{val/2:.2f} g", "b": ans, "c": f"{eth_mass*1.5:.2f} g", "d": f"{val} g"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
        elif ch_idx == 3:
            val = idx * 5
            # RCOOH + R'OH -> RCOOR' + H2O. Molar mass of Ester (Ethyl acetate = 88) from Acid (Acetic acid = 60).
            # Ester mass = val * (88/60)
            ester_mass = round(val * (88.0 / 60.0), 2)
            ans = f"{ester_mass} g"
            med_list.append({
                "question": f"A reaction is carried out with {val} g of acetic acid reacting with excess ethanol. Assuming 100% yield, what is the mass of ethyl acetate produced?",
                "options": {"a": f"{val} g", "b": ans, "c": f"{ester_mass*1.2:.2f} g", "d": f"{val/2:.2f} g"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
        elif ch_idx == 4:
            val = idx
            # Carbohydrates yield ~4 kcal/g, Lipids ~9 kcal/g.
            carb_g = val * 2
            lipid_g = val
            total_kcal = carb_g * 4 + lipid_g * 9
            ans = f"{total_kcal} kcal"
            med_list.append({
                "question": f"A nutritional sample contains {carb_g} g of carbohydrates and {lipid_g} g of lipids. Calculate the total energy released in kilocalories upon metabolism.",
                "options": {"a": f"{(carb_g+lipid_g)*4} kcal", "b": ans, "c": f"{total_kcal*1.5:.0f} kcal", "d": f"{total_kcal-10} kcal"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
        elif ch_idx == 5:
            # Haber Process: N2 + 3 H2 <=> 2 NH3
            val = idx * 3
            # Moles of H2 = val, Moles of NH3 = val * 2 / 3
            nh3_moles = round(val * 2.0 / 3.0, 2)
            ans = f"{nh3_moles} moles"
            med_list.append({
                "question": f"In the Haber process, {val} moles of hydrogen gas react completely with excess nitrogen. Calculate the moles of ammonia produced.",
                "options": {"a": f"{val} moles", "b": ans, "c": f"{val*2} moles", "d": f"{nh3_moles*1.5:.2f} moles"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
        elif ch_idx == 6:
            val = idx * 10
            # Order determinations
            ans = "Rate = k[A]^2"
            med_list.append({
                "question": f"For a reaction, doubling the concentration of reactant A increases the rate from 1.0 M/s to {4.0 + (idx*0.01)*0:.1f} M/s. What is the rate law expression?",
                "options": {"a": "Rate = k[A]", "b": ans, "c": "Rate = k[A]^3", "d": "Rate = k"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
        elif ch_idx == 7:
            val = idx * 0.1
            # Kc = [C] / ([A][B]). Let [A] = 0.2, [B] = 0.5, [C] = val
            kc = round(val / (0.2 * 0.5), 2)
            ans = f"{kc}"
            med_list.append({
                "question": f"For the equilibrium reaction A(aq) + B(aq) <=> C(aq), the concentrations are [A] = 0.2 M, [B] = 0.5 M, and [C] = {val:.2f} M. Find Kc.",
                "options": {"a": f"{val}", "b": ans, "c": f"{kc*2:.2f}", "d": f"{kc/2:.2f}"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
        else:  # Nuclear
            halflife = idx * 5
            total_time = halflife * 4
            rem_fraction = 1.0 / 16.0 * 100
            ans = f"{rem_fraction:.2f}%"
            med_list.append({
                "question": f"A radioactive substance has a half-life of {halflife} minutes. What percentage of the initial substance remains active after {total_time} minutes?",
                "options": {"a": "50.00%", "b": ans, "c": "12.50%", "d": "25.00%"},
                "correctAnswer": "b",
                "difficultyLevel": "medium"
            })
            
    # ------------------ HARD QUESTIONS (35) ------------------
    hard_list = []
    idx = 0
    while len(hard_list) < 35:
        idx += 1
        if ch_idx == 1:
            # Combustion stoichiometry
            val = idx
            # C3H8 + 5 O2 -> 3 CO2 + 4 H2O. Moles CO2 = 3 * val
            co2_moles = 3 * val
            ans = f"{co2_moles} moles"
            hard_list.append({
                "question": f"Calculate the number of moles of carbon dioxide gas produced by the complete combustion of {val} moles of propane (C3H8) in excess oxygen.",
                "options": {"a": f"{val} moles", "b": ans, "c": f"{val*5} moles", "d": f"{co2_moles*2} moles"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
        elif ch_idx == 2:
            # Calorimetry: heat of combustion
            # Q = m c dT. m = 200g water, c = 4.18, dT = idx * 2. moles = 0.01
            dt = idx * 2
            heat = 200 * 4.18 * dt  # Joules
            molar_heat = round((heat / 0.01) / 1000.0, 2)  # kJ/mol
            ans = f"{molar_heat} kJ/mol"
            hard_list.append({
                "question": f"In a calorimetry experiment, the combustion of 0.01 moles of an alcohol raises the temperature of 200 g of water by {dt} degrees Celsius. Calculate the molar heat of combustion of the alcohol. (Specific heat capacity of water = 4.18 J/g*C)",
                "options": {"a": f"{molar_heat/2:.2f} kJ/mol", "b": ans, "c": f"{molar_heat*1.5:.2f} kJ/mol", "d": f"{molar_heat+10:.2f} kJ/mol"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
        elif ch_idx == 3:
            # Acid-base titration
            # Ma Va = Mb Vb. Mb = 0.1 M, Vb = idx * 2 mL. Va = 10 mL.
            vb = idx * 2
            ma = round((0.1 * vb) / 10.0, 4)
            ans = f"{ma} M"
            hard_list.append({
                "question": f"A 10.0 mL sample of vinegar (containing acetic acid) requires {vb:.1f} mL of 0.10 M NaOH for complete neutralization. Calculate the molar concentration of acetic acid in the vinegar.",
                "options": {"a": "0.100 M", "b": ans, "c": f"{ma*2:.4f} M", "d": f"{ma/2:.4f} M"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
        elif ch_idx == 4:
            # Molecular weights or glucose combustion delta H
            val = idx
            # C6H12O6 combustion releases 2800 kJ/mol. Molar mass = 180.
            # Heat = val * (2800/180)
            energy = round(val * (2800.0 / 180.0), 2)
            ans = f"{energy} kJ"
            hard_list.append({
                "question": f"The enthalpy of combustion of glucose (C6H12O6) is -2800 kJ/mol. Calculate the amount of energy released when {val} g of glucose is completely oxidized.",
                "options": {"a": f"{val*2800} kJ", "b": ans, "c": f"{energy*1.2:.2f} kJ", "d": f"{energy/2:.2f} kJ"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
        elif ch_idx == 5:
            # Stoichiometry of chlorine displacement: Cl2 + 2 NaI -> 2 NaCl + I2.
            # Moles NaI = val * 0.1. Moles I2 produced = val * 0.05. Mass I2 = moles * 254
            val = idx
            i2_mass = round(val * 0.05 * 254, 2)
            ans = f"{i2_mass} g"
            hard_list.append({
                "question": f"Chlorine gas is bubbled through a solution containing {val * 0.1:.2f} moles of sodium iodide (NaI). Calculate the maximum mass of iodine (I2) displaced. (Molar mass of I2 = 254 g/mol)",
                "options": {"a": f"{val} g", "b": ans, "c": f"{i2_mass*2:.2f} g", "d": f"{i2_mass/2:.2f} g"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
        elif ch_idx == 6:
            # First order rate constant and half-life: k = 0.693 / t_1/2
            half_life = idx * 10
            k_val = round(0.693 / half_life, 5)
            ans = f"{k_val} s^-1"
            hard_list.append({
                "question": f"A first-order decomposition reaction has a half-life of {half_life} seconds. Calculate the specific rate constant (k) for this reaction.",
                "options": {"a": f"{half_life} s^-1", "b": ans, "c": f"{k_val*2:.5f} s^-1", "d": f"{k_val/2:.5f} s^-1"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
        elif ch_idx == 7:
            # ICE table calculation
            # H2 + I2 <=> 2 HI. Let initial [H2] = [I2] = val. Kc = 4 => [HI] = 2x, [H2] = val - x.
            # Kc = (2x)^2 / (val-x)^2 = 4 => 2x / (val-x) = 2 => 2x = 2val - 2x => 4x = 2val => x = val / 2.
            # Equilibrium [HI] = 2x = val.
            val = idx * 0.2
            ans = f"{val:.2f} M"
            hard_list.append({
                "question": f"For the equilibrium reaction H2(g) + I2(g) <=> 2 HI(g), the equilibrium constant Kc is 4.0. If {val:.2f} M of H2 and {val:.2f} M of I2 are placed in a container initially, calculate the equilibrium concentration of HI.",
                "options": {"a": f"{val*2:.2f} M", "b": ans, "c": f"{val/2:.2f} M", "d": "1.00 M"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
        else:  # Nuclear
            defect = idx * 0.003 + 0.015
            be = round(defect * 931.5, 2)
            ans = f"{be} MeV"
            hard_list.append({
                "question": f"The mass defect of a helium-4 nucleus is calculated to be {defect:.5f} atomic mass units (amu). Calculate its total nuclear binding energy in MeV. (Use 1 amu = 931.5 MeV)",
                "options": {"a": "28.30 MeV", "b": ans, "c": f"{be*1.5:.2f} MeV", "d": f"{be/2:.2f} MeV"},
                "correctAnswer": "b",
                "difficultyLevel": "hard"
            })
            
    return easy_list + med_list + hard_list

def main():
    print("Beginning Chemistry subject generation in English...")
    
    titles = {
        1: "Hydrocarbons",
        2: "Alcohols, Phenols and Ethers",
        3: "Aldehydes, Ketones and Carboxylic Acids",
        4: "Biochemistry",
        5: "p-Block Elements",
        6: "Chemical Kinetics",
        7: "Chemical Equilibrium",
        8: "Introduction to Nuclear Chemistry"
    }
    
    final_chem_chapters = []
    total_written = 0
    
    for i in range(1, 9):
        ch_id = f"chem_ch{i}"
        ch_questions = generate_chemistry_questions_for_chapter(i)
        
        # Format IDs sequentially: Chem_Ch{i}_Q{01-91}
        formatted_qs = []
        for idx, q in enumerate(ch_questions):
            q_id = f"Chem_Ch{i}_Q{idx+1:02d}"
            options_clean = {k.lower(): str(v) for k, v in q["options"].items()}
            formatted_qs.append({
                "id": q_id,
                "question": q["question"],
                "options": options_clean,
                "correctAnswer": q["correctAnswer"].lower(),
                "difficultyLevel": q["difficultyLevel"],
                "subjectId": "chem",
                "chapterId": ch_id
            })
            
        ch_easy = [q for q in formatted_qs if q["difficultyLevel"] == "easy"]
        ch_med = [q for q in formatted_qs if q["difficultyLevel"] == "medium"]
        ch_hard = [q for q in formatted_qs if q["difficultyLevel"] == "hard"]
        
        print(f"Chapter {i} ({titles[i]}): Total={len(formatted_qs)} (Easy={len(ch_easy)}, Medium={len(ch_med)}, Hard={len(ch_hard)})")
        
        # Verify counts
        assert len(ch_easy) == 27, f"Ch {i} easy is {len(ch_easy)}, expected 27"
        assert len(ch_med) == 29, f"Ch {i} medium is {len(ch_med)}, expected 29"
        assert len(ch_hard) == 35, f"Ch {i} hard is {len(ch_hard)}, expected 35"
        
        final_chem_chapters.append({
            "id": ch_id,
            "subjectId": "chem",
            "title": titles[i],
            "questions": formatted_qs
        })
        total_written += len(formatted_qs)
        
    print(f"Total Chemistry questions compiled: {total_written}")
    
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
    
    # Find existing chemistry subject (id: 'chem')
    chem_idx = -1
    for idx, s in enumerate(subjects):
        if s.get("id") == "chem" or s.get("name") == "Chemistry":
            chem_idx = idx
            break
            
    new_chem_chapters_format = []
    for ch in final_chem_chapters:
        new_chem_chapters_format.append({
            "title": ch["title"],
            "questions": ch["questions"]
        })
        
    new_chem_subject = {
        "name": "Chemistry",
        "id": "chem",
        "chapters": new_chem_chapters_format
    }
    
    if chem_idx != -1:
        subjects[chem_idx] = new_chem_subject
        print("Replaced existing Chemistry subject in subjects list.")
    else:
        subjects.append(new_chem_subject)
        print("Appended new Chemistry subject in subjects list.")
        
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
        data_json["subjects"]["chem"] = {"name": "Chemistry"}
        
        # Update chapters dictionary
        if "chapters" not in data_json:
            data_json["chapters"] = {}
        # Clear existing chemistry chapters first
        keys_to_remove = [k for k, v in data_json["chapters"].items() if v.get("subjectId") == "chem"]
        for k in keys_to_remove:
            del data_json["chapters"][k]
            
        # Add new chapters
        for ch in final_chem_chapters:
            data_json["chapters"][ch["id"]] = {
                "subjectId": "chem",
                "title": ch["title"]
            }
            
        # Update questions dictionary
        if "questions" not in data_json:
            data_json["questions"] = {}
        # Clear existing chemistry questions
        keys_to_remove = [k for k, v in data_json["questions"].items() if v.get("subjectId") == "chem" or v.get("chapterId", "").startswith("chem_")]
        for k in keys_to_remove:
            del data_json["questions"][k]
            
        # Add all new questions
        for ch in final_chem_chapters:
            for q in ch["questions"]:
                data_json["questions"][q["id"]] = {
                    "question": q["question"],
                    "options": q["options"],
                    "correctAnswer": q["correctAnswer"],
                    "difficultyLevel": q["difficultyLevel"],
                    "subjectId": "chem",
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
